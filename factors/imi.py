# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class IMIFactor(Factor):
    def signal(self, *args):
        """
        与 RSI 很相似。
        其区别在于，IMI 计算过程中使用的是收盘价和开盘价
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

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
        data[factor_name] = data["INC"] / (data["INC"] + data["DEC"])

        data = data.drop(columns=["INC", "DEC"])

        return data
