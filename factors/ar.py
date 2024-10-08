# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ARFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量开盘价在最高价、最低价之间的位置
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["high-open"] = data["high"] - data["open"]
        data["open-low"] = data["open"] - data["low"]
        data[self.factor_name] = (
            100 * cm.sum(data, "high-open", n) / cm.sum(data, "open-low", n)
        )

        data = data.drop(columns=["high-open", "open-low"])

        return data
