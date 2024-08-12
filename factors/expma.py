# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class EXPMAFactor(Factor):
    def signal(self, *args):
        """
        是简单移动平均的改进版，用于改善简单移动平均的滞后性问题
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        # factor_name = args[2]

        data["EMA1"] = cm.ema(data, N=n1)
        data["EMA2"] = cm.ema(data, N=n2)

        return data
