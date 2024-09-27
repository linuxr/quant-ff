# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class EXPMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        是简单移动平均的改进版，用于改善简单移动平均的滞后性问题
        """
        n1 = para[0]
        n2 = para[1]

        data["EMA1"] = cm.ema(data, N=n1)
        data["EMA2"] = cm.ema(data, N=n2)

        return data
