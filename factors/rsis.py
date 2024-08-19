# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class RSISFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        反映当前 RSI 在最近 N 天的 RSI 最大值和最小值之间的位置
        """
        n = para[0]
        m = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data["close-diff-pos"] = data.apply(
            lambda z: (
                z["close"] - z["ref-close"] if z["close"] > z["ref-close"] else 0
            ),
            axis=1,
        )
        data["abs"] = abs(data["close"] - data["ref-close"])
        data["RSI"] = (
            cm.sma(data, "close-diff-pos", n, 1) / cm.sma(data, "abs", n, 1) * 100
        )
        data["min-rsi"] = cm.min(data, "RSI", n)
        data["max-rsi"] = cm.max(data, "RSI", n)
        data[self.name] = (
            (data["RSI"] - data["min-rsi"]) / (data["max-rsi"] - data["min-rsi"]) * 100
        )
        data[f"{self.name}-MA"] = cm.ema(data, self.name, m)

        data = data.drop(
            columns=[
                "ref-close",
                "close-diff-pos",
                "abs",
                "RSI",
                "min-rsi",
                "max-rsi",
            ]
        )

        return data
