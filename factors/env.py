# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class ENVFactor(Factor):
    def signal(self, *args):
        """
        由移动平均线上下平移一定的幅度（百分比）所得
        """
        data = args[0]
        n = args[1][0]
        param = args[1][1]
        factor_name = args[2]

        data["mac"] = cm.ma(data, N=n)
        data[f"{factor_name}-UPPER"] = data["mac"] * (1 + param)
        data[f"{factor_name}-LOWER"] = data["mac"] * (1 - param)

        data = data.drop(columns=["mac"])

        return data
