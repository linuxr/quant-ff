# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MACDVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        MACD 的成交量版本
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = cm.ema(data, "volume", N=n1) - cm.ema(data, "volume", N=n2)
        # data["SIGNAL"] = cm.ema(data, "MACDVOL", N3)

        return data
