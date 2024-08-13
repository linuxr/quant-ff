# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class BOPFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量收盘价与开盘价的距离（正、负距离）占最高价与最低价的距离的比例
        """
        n = para[0]

        data["tmp"] = (data["close"] - data["open"]) / (data["high"] - data["low"])
        data[self.name] = cm.ma(data, "tmp", n)

        data = data.drop(columns=["tmp"])

        return data
