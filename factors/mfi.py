# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class MFIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 RSI 指标类似，
        不同的是，其在上升和下跌的条件判断用的是典型价格而不是收盘价，
        且其是对 MF 求和而不是收盘价的变化值
        """
        n = para[0]

        data["t-p"] = (data["high"] + data["low"] + data["close"]) / 3
        data["mf"] = data["t-p"] * data["volume"]
        data["ref-t-p"] = cm.ref(data, "t-p", 1)
        data["mf-pos"] = data.apply(
            lambda z: z["mf"] if z["t-p"] >= z["ref-t-p"] else 0,
            axis=1,
        )
        data["mf-pos"] = cm.sum(data, "mf-pos", n)

        data["mf-neg"] = data.apply(
            lambda z: z["mf"] if z["t-p"] <= z["ref-t-p"] else 0,
            axis=1,
        )
        data["mf-neg"] = cm.sum(data, "mf-neg", n)
        data[self.name] = 100 - 100 / (1 + data["mf-pos"] / data["mf-neg"])

        data = data.drop(
            columns=[
                "t-p",
                "mf",
                "ref-t-p",
                "mf-pos",
                "mf-neg",
            ]
        )

        return data
