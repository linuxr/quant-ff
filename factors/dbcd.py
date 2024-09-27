# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DBCDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        乖离率离差的移动平均
        """
        n = para[0]
        m = para[1]
        t = para[2]

        data["bias"] = 100 * (data["close"] - cm.ma(data, N=n)) / cm.ma(data, N=n)
        data["ref-bias"] = cm.ref(data, "bias", m)
        data["bias-diff"] = data["bias"] - data["ref-bias"]
        data[self.name] = cm.sma(data, "bias-diff", t, 1)

        data = data.drop(columns=["ref-bias", "bias-diff", "bias"])

        return data
