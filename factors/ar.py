# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class ARFactor(Factor):
    def signal(self, *args):
        """
        衡量开盘价在最高价、最低价之间的位置
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["high-open"] = data["high"] - data["open"]
        data["open-low"] = data["open"] - data["low"]
        data[factor_name] = (
            100 * cm.sum(data, "high-open", n) / cm.sum(data, "open-low", n)
        )

        data = data.drop(columns=["high-open", "open-low"])

        return data
