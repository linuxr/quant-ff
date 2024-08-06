# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIASFactor(Factor):
    def signal(self, *args):
        """
        衡量收盘价与移动平均线之间的差距
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data[factor_name] = 100 * (data["close"] - cm.ma(data, N=n)) / cm.ma(data, N=n)

        return data
