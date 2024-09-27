# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class TMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与其他的均线类似，不同的是，TMA 则赋予考虑的时间段内时间靠中间的价格更高的权重
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["close-ma"] = cm.ma(data, N=n)
        data[self.factor_name] = cm.ma(data, "close-ma", n)

        data = data.drop(columns=["close-ma"])

        return data
