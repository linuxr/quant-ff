# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class TRIXFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        价格的三重指数移动平均的变化率
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ema"] = cm.ema(data, N=n)
        data["ema"] = cm.ema(data, "ema", n)
        data["ema"] = cm.ema(data, "ema", n)

        data["ref-ema"] = cm.ref(data, "ema", 1)
        data[self.factor_name] = (data["ema"] - data["ref-ema"]) / data["ref-ema"]

        data = data.drop(columns=["ema", "ref-ema"])

        return data
