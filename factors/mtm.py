# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MTMFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用当天价格与 N 天前价格的差值来衡量价格的动量
        """
        n = para[0]

        data[self.name] = data["close"] - cm.ref(data, N=n)

        return data
