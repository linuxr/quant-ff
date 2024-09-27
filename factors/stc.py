# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class STCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        结合了 MACD 指标和 KDJ 指标的算法
        """
        n = para[0]
        n1 = para[1]
        n2 = para[2]

        data["macdx"] = cm.ema(data, N=n1) - cm.ema(data, N=n2)
        data["v1"] = cm.min(data, "macdx", n)
        data["v2"] = cm.max(data, "macdx", n) - data["v1"]

        data = data.reset_index()
        data["fk"] = (data["macdx"] - data["v1"]) / data["v2"] * 100
        for idx, _ in data[1:].iterrows():
            if data.loc[idx, "v2"] > 0:
                continue

            data.loc[idx, "fk"] = data.loc[idx - 1, "fk"]

        data["fd"] = cm.sma(data, "fk", n, 1)
        data["v3"] = cm.min(data, "fd", n)
        data["v4"] = cm.max(data, "fd", n) - data["v3"]

        data["sk"] = (data["fd"] - data["v3"]) / data["v4"] * 100
        for idx, _ in data[1:].iterrows():
            if data.loc[idx, "v4"] > 0:
                continue

            data.loc[idx, "sk"] = data.loc[idx - 1, "sk"]

        data[self.name] = cm.sma(data, "sk", n, 1)

        data = data.drop(
            columns=[
                "macdx",
                "v1",
                "v2",
                "fk",
                "fd",
                "v3",
                "v4",
                "sk",
            ]
        )

        return data
