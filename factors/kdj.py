# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class KDJFactor(Factor):
    def signal(self, *args):
        """
        用来衡量当前收盘价在过去 N 天的最低价与最高价之间的位置
        """
        data = args[0]
        n = args[1][0]
        # factor_name = args[2]

        data["low-n"] = cm.min(data, "low", n)
        data["high-n"] = cm.max(data, "high", n)
        data["Stochastics"] = (
            (data["close"] - data["low-n"]) / (data["high-n"] - data["low-n"]) * 100
        )
        data["K"] = cm.sma(data, "Stochastics", 3, 1)
        data["D"] = cm.sma(data, "K", 3, 1)

        data = data.drop(columns=["low-n", "high-n", "Stochastics"])

        return data
