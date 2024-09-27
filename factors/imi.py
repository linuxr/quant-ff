# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class IMIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 RSI 很相似。
        其区别在于，IMI 计算过程中使用的是收盘价和开盘价
        """
        n = para[0]

        data["INC"] = data.apply(
            lambda z: (z["close"] - z["open"] if z["close"] > z["open"] else 0),
            axis=1,
        )
        data["INC"] = cm.sum(data, "INC", n)

        data["DEC"] = data.apply(
            lambda z: (z["open"] - z["close"] if z["open"] > z["close"] else 0),
            axis=1,
        )
        data["DEC"] = cm.sum(data, "DEC", n)
        data[self.name] = data["INC"] / (data["INC"] + data["DEC"])

        data = data.drop(columns=["INC", "DEC"])

        return data
