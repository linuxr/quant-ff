# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class WRFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        事实上就是 100-KDJ 指标计算过程中的 Stochastics
        WR指标用来衡量市场的强弱和超买超卖状态
        """
        n = para[0]

        data["h"] = cm.max(data, "high", n)
        data["l"] = cm.min(data, "low", n)
        data[self.name] = 100 * (data["h"] - data["close"]) / (data["h"] - data["l"])

        data = data.drop(columns=["h", "l"])

        return data
