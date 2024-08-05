# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class BRFactor(Factor):
    def signal(self, *args):
        """
        衡量昨日收盘价在今日最高价、最低价之间的位置
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["high-refclose"] = data["high"] - data["ref-close"]
        data["refclose-low"] = data["ref-close"] - data["low"]
        data[factor_name] = (
            100 * cm.sum(data, "high-refclose", n) / cm.sum(data, "refclose-low", n)
        )

        data = data.drop(
            columns=[
                "ref-close",
                "high-refclose",
                "refclose-low",
            ]
        )

        return data
