# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIAS36Factor(Factor):
    def signal(self, *args):
        """
        用来衡量不同的移动平均价间的差距
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["36"] = cm.ma(data, N=3) - cm.ma(data, N=6)
        data[factor_name] = cm.ma(data, "36", n)

        data = data.drop(columns=["36"])

        return data
