# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class PSYFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        过去 N 天股价上涨的天数的比例*100，用来衡量投资者心理和市场的人气
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data[self.name] = data.apply(
            lambda z: 1 if z["close"] > z["ref-close"] else 0,
            axis=1,
        )
        data[self.name] = data[self.name] / n * 100

        data = data.drop(columns=["ref-close"])

        return data
