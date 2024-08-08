# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DPOFactor(Factor):
    def signal(self, *args):
        """
        当前价格与延迟的移动平均线的差值
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["close-ma"] = cm.ma(data, N=n)
        data[factor_name] = data["close"] - cm.ref(data, "close-ma", n // 2 + 1)

        data = data.drop(columns=["close-ma"])

        return data
