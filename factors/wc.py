# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class WCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        可以用来代替收盘价构造一些技术指标（不过相对比较少用到）
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = (data["high"] + data["low"] + 2 * data["close"]) / 4
        data[f"{self.name}-EMA1"] = cm.ema(data, self.name, n1)
        data[f"{self.name}-EMA2"] = cm.ema(data, self.name, n2)

        return data
