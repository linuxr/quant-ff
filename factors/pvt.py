# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class PVTFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用价格的变化率作为权重求成交量的移动平均
        """
        n1 = para[0]
        n2 = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data[self.name] = (
            (data["close"] - data["ref-close"]) / data["ref-close"] * data["volume"]
        )
        data[f"{self.name}-MA1"] = cm.ma(data, self.name, n1)
        data[f"{self.name}-MA2"] = cm.ma(data, self.name, n2)

        data = data.drop(columns=["X"])

        return data
