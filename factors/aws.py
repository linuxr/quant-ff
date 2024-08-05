# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class AWSFactor(Factor):
    def signal(self, *args):
        """
        MACD 指标的变形，将其中的收盘价改为最高价与最低价的均值
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        n3 = args[1][2]
        factor_name = args[2]

        data["avg-hl"] = (data["high"] + data["low"]) / 2
        data[factor_name] = cm.ema(data, "avg-hl", n1) - cm.ema(data, "avg-hl", n2)
        data["SIGNAL"] = cm.ema(data, factor_name, n3)
        data["HISTOGRAM"] = data[factor_name] - data["SIGNAL"]

        data = data.drop(columns=["avg-hl"])

        return data
