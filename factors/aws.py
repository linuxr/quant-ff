# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class AWSFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        MACD 指标的变形，将其中的收盘价改为最高价与最低价的均值
        """
        n1 = para[0]
        n2 = para[1]
        n3 = para[2]

        data["avg-hl"] = (data["high"] + data["low"]) / 2
        data[self.name] = cm.ema(data, "avg-hl", n1) - cm.ema(data, "avg-hl", n2)
        data["SIGNAL"] = cm.ema(data, self.name, n3)
        data["HISTOGRAM"] = data[self.name] - data["SIGNAL"]

        data = data.drop(columns=["avg-hl"])

        return data
