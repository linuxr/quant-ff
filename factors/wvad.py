# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class WVADFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用价格信息对成交量加权的价量指标，用来比较开盘到收盘期间多空双方的力量
        """
        n = para[0]

        data[self.name] = (
            (data["close"] - data["open"])
            / (data["high"] - data["low"])
            * data["volume"]
        )
        data[self.name] = cm.sum(data, self.name, n)

        return data
