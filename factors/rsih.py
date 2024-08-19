# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class RSIHFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        对 RSI 作移动平均得到 RSI_SIGNAL，取两者的差得到 RSI HISTOGRAM
        """
        n1 = para[0]
        n2 = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data["close-diff-pos"] = data.apply(
            lambda z: (
                z["close"] - z["ref-close"] if z["close"] > z["ref-close"] else 0
            ),
            axis=1,
        )
        data["abs"] = abs(data["close"] - data["ref-close"])
        data["RSI"] = (
            cm.sma(data, "close-diff-pos", n1, 1) / cm.sma(data, "abs", n1, 1) * 100
        )
        data["SIGNAL"] = cm.ema(data, "RSI", n2)
        data[self.name] = data["RSI"] - data["SIGNAL"]

        data = data.drop(
            columns=[
                "ref-close",
                "close-diff-pos",
                "abs",
                "RSI",
                "SIGNAL",
            ]
        )

        return data
