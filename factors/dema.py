# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DEMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        结合了单重 EMA 和双重 EMA，在保证平滑性的同时减少滞后性
        """
        n = para[0]

        data["EMA"] = cm.ema(data, N=n)
        data[self.name] = 2 * data["EMA"] - cm.ema(data, "EMA", n)

        data = data.drop(columns=["EMA"])

        return data
