# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ASIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        对 SI 累计求和得到 ASI
        """
        n = para[0]
        m = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data["ref-low"] = cm.ref(data, "low", N=1)
        data["ref-open"] = cm.ref(data, "open", N=1)

        data["a"] = abs(data["high"] - data["ref-close"])
        data["b"] = abs(data["low"] - data["ref-close"])
        data["c"] = abs(data["high"] - data["ref-low"])
        data["d"] = abs(data["ref-close"] - data["ref-open"])
        data["k"] = data.apply(lambda z: max(z["a"], z["b"]), axis=1)
        data["high-low"] = data["high"] - data["low"]
        data["m"] = cm.max(data, "high-low", n)

        data["r1"] = data["a"] + 0.5 * data["b"] + 0.25 * data["d"]
        data["r2"] = data["b"] + 0.5 * data["a"] + 0.25 * data["d"]
        data["r3"] = data["c"] + 0.25 * data["d"]
        data["r4"] = data.apply(
            lambda z: z["r1"] if z["a"] >= z["b"] and z["a"] >= z["c"] else z["r2"],
            axis=1,
        )
        data["r"] = data.apply(
            lambda z: z["r3"] if z["c"] >= z["a"] and z["c"] >= z["b"] else z["r4"],
            axis=1,
        )
        data["SI"] = (
            50
            * (
                data["close"]
                - data["ref-close"]
                + (data["ref-close"] - data["ref-open"])
                + 0.5 * (data["close"] - data["open"])
            )
            / data["r"]
            * data["k"]
            / data["m"]
        )
        data[self.name] = cm.cumsum(data, "SI")
        data[f"{self.name}MA"] = cm.ma(data, self.name, m)

        data = data.drop(
            columns=[
                "ref-close",
                "ref-low",
                "ref-open",
                "a",
                "b",
                "c",
                "d",
                "k",
                "high-low",
                "m",
                "r1",
                "r2",
                "r3",
                "r4",
                "r",
                "SI",
            ]
        )

        return data
