# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class QsitckFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        通过比较收盘价与开盘价来反映股价趋势的方向和强度
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["close-open"] = data["close"] - data["open"]
        data[self.factor_name] = cm.ma(data, "close-open", n)

        data = data.drop(columns=["close-open"])

        return data
