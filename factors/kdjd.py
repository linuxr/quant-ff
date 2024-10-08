# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class KDJDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        可以看作 KDJ 的变形
        """
        n = para[0]
        m = para[1]

        data["low-n"] = cm.min(data, "low", n)
        data["high-n"] = cm.max(data, "high", n)
        data["Stochastics"] = (
            (data["close"] - data["low-n"]) / (data["high-n"] - data["low-n"]) * 100
        )
        data["Stochastics-low"] = cm.min(data, "Stochastics", m)
        data["Stochastics-high"] = cm.max(data, "Stochastics", m)
        data["Stochastics-double"] = (
            (data["Stochastics"] - data["Stochastics-low"])
            / (data["Stochastics-high"] - data["Stochastics-low"])
            * 100
        )
        data["K"] = cm.sma(data, "Stochastics-double", 3, 1)
        data["D"] = cm.sma(data, "K", 3, 1)

        data = data.drop(
            columns=[
                "low-n",
                "high-n",
                "Stochastics",
                "Stochastics-double",
                "Stochastics-low",
                "Stochastics-high",
            ]
        )

        return data
