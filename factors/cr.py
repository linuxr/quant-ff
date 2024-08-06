# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class CRFactor(Factor):
    def signal(self, *args):
        """
        与 AR、BR 类似。CR 通过比较最高价、最低价和典型价格来衡量市场人气
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["typ"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ref-typ"] = cm.ref(data, "typ", 1)
        data["h"] = data.apply(
            lambda z: max(z["high"] - z["ref-typ"], 0),
            axis=1,
        )
        data["l"] = data.apply(
            lambda z: max(z["ref-typ"] - z["low"], 0),
            axis=1,
        )
        data[factor_name] = 100 * cm.sum(data, "h", n) / cm.sum(data, "l", n)

        data = data.drop(columns=["typ", "ref-typ", "h", "l"])

        return data
