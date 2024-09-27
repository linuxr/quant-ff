# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class APZFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        根据价格波动性围绕均线而制成的价格通道
        """
        n = para[0]
        m = para[1]
        param = para[2]

        data["high-low"] = data["high"] - data["low"]
        data["ema-high-low"] = cm.ema(data, "high-low", n)
        data["vol"] = cm.ema(data, "ema-high-low", n)

        data["ema-close"] = cm.ema(data, "close", m)
        data[f"{self.name}-UPPER"] = cm.ema(data, "ema-close", m) + param * data["vol"]
        data[f"{self.name}-LOWER"] = cm.ema(data, "ema-close", m) - param * data["vol"]

        data = data.drop(
            columns=[
                "high-low",
                "ema-high-low",
                "vol",
                "ema-close",
            ]
        )

        return data
