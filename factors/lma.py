# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class LMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        简单移动平均线把收盘价替换为最低价
        """
        n = para[0]

        data[self.name] = cm.ma(data, "low", n)

        return data
