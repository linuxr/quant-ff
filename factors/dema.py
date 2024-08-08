# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DEMAFactor(Factor):
    def signal(self, *args):
        """
        结合了单重 EMA 和双重 EMA，在保证平滑性的同时减少滞后性
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["EMA"] = cm.ema(data, N=n)
        data[factor_name] = 2 * data["EMA"] - cm.ema(data, "EMA", n)

        data = data.drop(columns=["EMA"])

        return data
