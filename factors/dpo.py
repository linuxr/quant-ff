# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class DPOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        当前价格与延迟的移动平均线的差值
        """
        n = para[0]

        data["close-ma"] = cm.ma(data, N=n)
        data[self.name] = data["close"] - cm.ref(data, "close-ma", n // 2 + 1)

        data = data.drop(columns=["close-ma"])

        return data
