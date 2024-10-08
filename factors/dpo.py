# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DPOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        当前价格与延迟的移动平均线的差值
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["close-ma"] = cm.ma(data, N=n)
        data[self.factor_name] = data["close"] - cm.ref(data, "close-ma", n // 2 + 1)

        data = data.drop(columns=["close-ma"])

        return data
