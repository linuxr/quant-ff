# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BOPFactor(Factor):
    def signal(self, *args):
        """
        衡量收盘价与开盘价的距离（正、负距离）占最高价与最低价的距离的比例
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["tmp"] = (data["close"] - data["open"]) / (data["high"] - data["low"])
        data[factor_name] = cm.ma(data, "tmp", n)

        data = data.drop(columns=["tmp"])

        return data
