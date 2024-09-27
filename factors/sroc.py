# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class SROCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡衡量价格的涨跌幅
        """
        n = para[0]
        m = para[1]

        data["emap"] = cm.ema(data, N=n)
        data["ref-emap"] = cm.ref(data, "emap", m)
        data[self.name] = (data["emap"] - data["ref-emap"]) / data["ref-emap"]

        data = data.drop(columns=["emap", "ref-emap"])

        return data
