# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class FIFactor(Factor):
    def signal(self, *args):
        """
        用价格的变化来衡量价格的趋势，用成交量大小来衡量趋势的强弱
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["ref-close"] = cm.ref(data, N=1)
        data[factor_name] = (data["close"] - data["ref-close"]) * data["volume"]
        data[f"{factor_name}MA"] = cm.ema(data, factor_name, n)

        data = data.drop(columns=["ref-close"])

        return data
