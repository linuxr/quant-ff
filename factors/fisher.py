# -*- coding=utf-8 -*-

import quant_ff.common as cm
import numpy as np
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class FISHERFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用来衡量当前价位于过去 N 天的最高价和最低价之间的位置
        """
        n = para[0]
        param = para[1]

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
        data[self.name] = 0.5 * np.log(
            (1 + data["price-change"]) / (1 - data["price-change"])
        )
        data[self.name] = 0.5 * cm.ref(data, self.name, 1)

        data = data.drop(columns=["price", "price-change"])

        return data
