# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class TEMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        结合了单重、双重和三重的 EMA，相比于一般均线延迟性较低
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ema-c"] = cm.ema(data, N=n)
        data["ema-cc"] = cm.ema(data, "ema-c", n)
        data[self.factor_name] = (
            3 * data["ema-c"] - 3 * data["ema-cc"] + cm.ema(data, "ema-cc", n)
        )

        data = data.drop(columns=["ema-c", "ema-cc"])

        return data
