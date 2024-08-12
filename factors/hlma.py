# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class HLMAFactor(Factor):
    def signal(self, *args):
        """
        由移动平均线上下平移一定的幅度（百分比）所得
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        # factor_name = args[2]

        data["HMA"] = cm.ma(data, "high", N=n1)
        data["LMA"] = cm.ma(data, "low", N=n2)

        return data
