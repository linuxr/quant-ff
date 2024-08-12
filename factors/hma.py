# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class HMAFactor(Factor):
    def signal(self, *args):
        """
        简单移动平均线把收盘价替换为最高价
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data[factor_name] = cm.ma(data, "high", n)

        return data
