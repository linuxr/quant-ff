# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BBIFactor(Factor):
    def signal(self, *args):
        """
        对不同时间长度的移动平均线取平均，
        能够综合不同移动平均线的平滑性和滞后性
        """
        data = args[0]
        # n = args[1][0]
        factor_name = args[2]

        data[factor_name] = (
            cm.ma(data, N=3) + cm.ma(data, N=6) + cm.ma(data, N=12) + cm.ma(data, N=24)
        ) / 4

        return data
