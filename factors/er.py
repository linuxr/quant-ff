# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ERFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        动量指标。用来衡量市场的多空力量对比
        """
        n = para[0]

        data["ema-close"] = cm.ema(data, N=n)
        data["BullPower"] = data["high"] - data["ema-close"]
        data["BearPower"] = data["low"] - data["ema-close"]

        # data = data.drop(columns=["mac"])

        return data
