# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DDIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用来比较向上波动和向下波动的比例
        """
        n = para[0]

        data["hl"] = data["high"] + data["low"]
        data["ref-h"] = cm.ref(data, "high", 1)
        data["ref-l"] = cm.ref(data, "low", 1)
        data["ref-hl"] = cm.ref(data, "hl", 1)
        data["high-abs"] = abs(data["high"] - data["ref-h"])
        data["low-abs"] = abs(data["low"] - data["ref-l"])

        data["DMZ"] = data.apply(
            lambda z: max(z["high-abs"], z["low-abs"]) if z["hl"] > z["ref-hl"] else 0,
            axis=1,
        )
        data["DMF"] = data.apply(
            lambda z: max(z["high-abs"], z["low-abs"]) if z["hl"] < z["ref-hl"] else 0,
            axis=1,
        )
        data["DIZ"] = cm.sum(data, "DMZ", n) / (
            cm.sum(data, "DMZ", n) + cm.sum(data, "DMF", n)
        )
        data["DIF"] = cm.sum(data, "DMF", n) / (
            cm.sum(data, "DMZ", n) + cm.sum(data, "DMF", n)
        )
        data[self.name] = data["DIZ"] - data["DIF"]

        data = data.drop(
            columns=[
                "hl",
                "ref-h",
                "ref-l",
                "ref-hl",
                "high-abs",
                "low-abs",
                "DMZ",
                "DMF",
                "DIZ",
                "DIF",
            ]
        )

        return data
