# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        具有趋势的特性，它比较平稳，不像日K线会起起落落地震荡
        """
        n = para[0]

        data[self.name] = cm.ma(data, N=n)

        return data
