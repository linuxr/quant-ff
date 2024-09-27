# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VAOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 PVT 类似，都综合考虑成交量和价格,以价格的变化为权重对成交量进行加权
        """
        n1 = para[0]
        n2 = para[1]

        data["w-vol"] = data["volume"] * (
            data["close"] - (data["high"] + data["low"]) / 2
        )
        data[self.name] = data["w-vol"]
        data[self.name] = data[self.name] + cm.ref(data, self.name, 1)
        data[f"{self.name}-MA1"] = cm.ma(data, self.name, n1)
        data[f"{self.name}-MA2"] = cm.ma(data, self.name, n2)

        data = data.drop(columns=["w-vol"])

        return data
