# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class POSFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量当前的 N 天收益率在过去 N 天的 N 天收益率最大值和最小值之间的位置
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-close"] = cm.ref(data, N=n)
        data["price"] = (data["close"] - data["ref-close"]) / data["ref-close"]
        data["price-min"] = cm.min(data, "price", n)
        data["price-max"] = cm.max(data, "price", n)
        data[self.factor_name] = (data["price"] - data["price-min"]) / (
            data["price-max"] - data["price-min"]
        )

        data = data.drop(columns=["ref-close", "price", "price-min", "price-max"])

        return data
