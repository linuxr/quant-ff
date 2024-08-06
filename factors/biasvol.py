# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIASVOLFactor(Factor):
    def signal(self, *args):
        """
        BIAS 指标的成交量版本
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data[factor_name] = (data["volume"] - cm.ma(data, "volume", n)) / cm.ma(
            data, "volume", n
        )

        return data
