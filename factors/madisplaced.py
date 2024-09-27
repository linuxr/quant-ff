# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MADisplacedFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        把简单移动平均线向前移动了 M 个交易日，用法与一般的移动平均线一样
        """
        n = para[0]
        m = para[1]

        data["ma-close"] = cm.ma(data, N=n)
        data[self.name] = cm.ref(data, "ma-close", m)

        data = data.drop(columns=["ma-close"])

        return data
