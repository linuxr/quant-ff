# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class MACDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量快速均线与慢速均线的差值
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = cm.ema(data, N=n1) - cm.ema(data, N=n2)
        # data["SIGNAL"] = cm.ema(data, "MACD", N3)
        # data["HISTOGRAM"] = data["MACD"] - data["SIGNAL"]

        return data
