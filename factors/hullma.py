# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class HULLMAFactor(Factor):
    def signal(self, *args):
        """
        均线的一种，相比于普通均线有着更低的延迟性
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["X"] = 2 * cm.ema(data, N=n // 2) - cm.ema(data, N=n)

        import math

        data[factor_name] = cm.ema(data, "X", round(math.sqrt(n)))

        data = data.drop(columns=["X"])

        return data
