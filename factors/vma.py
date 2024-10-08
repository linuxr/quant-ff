# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        简单移动平均把收盘价替换为最高价、最低价、开盘价和收盘价的平均值
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["PRICE"] = (data["high"] + data["low"] + data["open"] + data["close"]) / 4
        data[self.factor_name] = cm.ma(data, "PRICE", n)

        data = data.drop(columns=["PRICE"])

        return data
