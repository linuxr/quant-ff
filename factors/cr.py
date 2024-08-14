# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class CRFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 AR、BR 类似。CR 通过比较最高价、最低价和典型价格来衡量市场人气
        """
        n = para[0]

        data["typ"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ref-typ"] = cm.ref(data, "typ", 1)
        data["h"] = data.apply(
            lambda z: max(z["high"] - z["ref-typ"], 0),
            axis=1,
        )
        data["l"] = data.apply(
            lambda z: max(z["ref-typ"] - z["low"], 0),
            axis=1,
        )
        data[self.name] = 100 * cm.sum(data, "h", n) / cm.sum(data, "l", n)

        data = data.drop(columns=["typ", "ref-typ", "h", "l"])

        return data
