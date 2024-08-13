# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIASFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量收盘价与移动平均线之间的差距
        """
        n = para[0]

        data[self.name] = 100 * (data["close"] - cm.ma(data, N=n)) / cm.ma(data, N=n)

        return data
