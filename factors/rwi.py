# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass
import math


@dataclass
class RWIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        对一段时间股票的随机漫步区间与真实运动区间进行比较以判断股票价格的走势
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["abs1"] = abs(data["high"] - data["low"])
        data["abs2"] = abs(data["high"] - data["ref-close"])
        data["abs3"] = abs(data["ref-close"] - data["low"])
        data["tr"] = data.apply(
            lambda z: max(z["abs1"], z["abs2"], z["abs3"]),
            axis=1,
        )

        data["atr"] = cm.ma(data, "tr", n)
        data[f"{self.name}-HIGH"] = (data["high"] - cm.ref(data, "low", 1)) / (
            data["atr"] * math.sqrt(n)
        )
        data[f"{self.name}-LOW"] = (cm.ref(data, "high", 1) - data["low"]) / (
            data["atr"] * math.sqrt(n)
        )

        data = data.drop(
            columns=[
                "ref-close",
                "abs1",
                "abs2",
                "abs3",
                "tr",
                "atr",
            ]
        )

        return data
