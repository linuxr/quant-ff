# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class TYPFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        典型价格（最高价+最低价+收盘价）/3 经常被用来代替收盘价
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = (data["close"] + data["high"] + data["low"]) / 3
        data[f"{self.name}-MA1"] = cm.ema(data, self.name, n1)
        data[f"{self.name}-MA2"] = cm.ema(data, self.name, n2)

        return data
