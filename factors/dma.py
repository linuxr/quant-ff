# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DMAFactor(Factor):
    def signal(self, *args):
        """
        衡量快速移动平均与慢速移动平均之差
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        factor_name = args[2]

        data[factor_name] = cm.ma(data, N=n1) - cm.ma(data, N=n2)
        # data["AMA"] = cm.ma(data, factor_name, N=n1)

        return data
