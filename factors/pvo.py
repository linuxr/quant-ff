# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class PVOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用成交量的指数移动平均来反应成交量的变化
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = (
            cm.ema(data, "volume", n1) - cm.ema(data, "volume", n2)
        ) / cm.ema(data, "volume", n2)

        return data
