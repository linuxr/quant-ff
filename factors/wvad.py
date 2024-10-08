# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class WVADFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用价格信息对成交量加权的价量指标，用来比较开盘到收盘期间多空双方的力量
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data[self.factor_name] = (
            (data["close"] - data["open"])
            / (data["high"] - data["low"])
            * data["volume"]
        )
        data[self.factor_name] = cm.sum(data, self.factor_name, n)

        return data
