# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class SKDJFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        慢速随机波动（即慢速 KDJ）
        """
        n = para[0]

        data["min-low"] = cm.min(data, "low", n)
        data["max-high"] = cm.max(data, "high", n)
        data["RSV"] = (
            (data["close"] - data["min-low"])
            / (data["max-high"] - data["min-low"])
            * 100
        )
        data["MARSV"] = cm.sma(data, "RSV", 3, 1)
        data["K"] = cm.sma(data, "MARSV", 3, 1)
        data["D"] = cm.ma(data, "K", 3)

        data = data.drop(columns=["min-low", "max-high", "RSV", "MARSV"])

        return data
