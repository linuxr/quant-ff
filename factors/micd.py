# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MICDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        异同离差动力指数
        """
        n = para[0]
        n1 = para[1]
        n2 = para[2]
        m = para[3]

        data["ref-close"] = cm.ref(data, N=1)
        data["mi"] = data["close"] - data["ref-close"]
        data["mtmma"] = cm.sma(data, "mi", n, 1)
        data["ref-mtmma"] = cm.ref(data, "mtmma", 1)
        data["dif"] = cm.ma(data, "ref-mtmma", n1) - cm.ma(data, "ref-mtmma", n2)
        data[self.name] = cm.sma(data, "dif", m, 1)

        data = data.drop(columns=["ref-close", "mi", "mtmma", "ref-mtmma", "dif"])

        return data
