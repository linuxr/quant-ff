# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class CLVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量收盘价在最低价和最高价之间的位置
        """
        n = para[0]

        data[self.name] = (2 * data["close"] - data["low"] - data["close"]) / (
            data["high"] - data["low"]
        )
        data[f"{self.name}MA"] = cm.ma(data, self.name, n)

        return data
