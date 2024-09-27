# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class KDJFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用来衡量当前收盘价在过去 N 天的最低价与最高价之间的位置
        """
        n = para[0]

        data["low-n"] = cm.min(data, "low", n)
        data["high-n"] = cm.max(data, "high", n)
        data["Stochastics"] = (
            (data["close"] - data["low-n"]) / (data["high-n"] - data["low-n"]) * 100
        )
        data["K"] = cm.sma(data, "Stochastics", 3, 1)
        data["D"] = cm.sma(data, "K", 3, 1)

        data = data.drop(columns=["low-n", "high-n", "Stochastics"])

        return data
