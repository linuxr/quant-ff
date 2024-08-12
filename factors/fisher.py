# -*- coding=utf-8 -*-

import common as cm
import numpy as np

from factors import Factor
from dataclasses import dataclass


@dataclass
class FISHERFactor(Factor):
    def signal(self, *args):
        """
        用来衡量当前价位于过去 N 天的最高价和最低价之间的位置
        """
        data = args[0]
        n = args[1][0]
        param = args[1][1]
        factor_name = args[2]

        data["price"] = (data["high"] + data["low"]) / 2
        data["price-change"] = 2 * (
            data["price"]
            - cm.min(data, "low", n)
            / (cm.max(data, "high", n) - cm.min(data, "low", n))
            - 0.5
        )
        data["price-change"] = data["price-change"].apply(
            lambda z: 0.999 if z > 0.99 else z
        )
        data["price-change"] = data["price-change"].apply(
            lambda z: -0.999 if z < -0.99 else z
        )
        data["price-change"] = param * data["price-change"] + (1 - param) * cm.ref(
            data, "price-change", 1
        )
        data[factor_name] = 0.5 * np.log(
            (1 + data["price-change"]) / (1 - data["price-change"])
        )
        data[factor_name] = 0.5 * cm.ref(data, factor_name, 1)

        data = data.drop(columns=["price", "price-change"])

        return data
