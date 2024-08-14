# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class KCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与布林带类似，都是用价格的移动平均构造中轨，
        不同的是表示波幅的方法，这里用 ATR 来作为波幅构造上下轨
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["ref-low"] = cm.ref(data, "low", N=1)
        data["tr"] = data.apply(
            lambda z: max(
                abs(z["high"] - z["low"]),
                abs(z["high"] - z["ref-close"]),
                abs(z["ref-close"] - z["ref-low"]),
            ),
            axis=1,
        )
        data["atr"] = cm.ma(data, "tr", n)
        data["middle"] = cm.ema(data, N=20)
        data["UPPER"] = data["middle"] + data["atr"] * 2
        data["LOWER"] = data["middle"] - data["atr"] * 2

        data = data.drop(columns=["ref-close", "ref-low", "tr", "atr", "middle"])

        return data
