# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class FIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用价格的变化来衡量价格的趋势，用成交量大小来衡量趋势的强弱
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data[self.name] = (data["close"] - data["ref-close"]) * data["volume"]
        data[f"{self.name}MA"] = cm.ema(data, self.name, n)

        data = data.drop(columns=["ref-close"])

        return data
