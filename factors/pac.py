# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class PACFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用最高价和最低价的移动平均来构造价格变化的通道
        """
        n1 = para[0]
        n2 = para[1]

        data["UPPER"] = cm.sma(data, "high", n1, 1)
        data["LOWER"] = cm.sma(data, "low", n2, 1)

        return data
