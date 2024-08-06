# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class CLVFactor(Factor):
    def signal(self, *args):
        """
        衡量收盘价在最低价和最高价之间的位置
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data[factor_name] = (2 * data["close"] - data["low"] - data["close"]) / (
            data["high"] - data["low"]
        )
        data[f"{factor_name}MA"] = cm.ma(data, factor_name, n)

        return data
