# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DZRSIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        动态的 RSI，原理与 DZCCI 相同，计算公式为 DZCCI 中的CCI 替换为 RSI
        """
        n = para[0]
        m = para[1]
        param = para[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["closeup"] = data.apply(
            lambda z: (
                z["close"] - z["ref-close"] if z["close"] > z["ref-close"] else 0
            ),
            axis=1,
        )
        data["closedown"] = data.apply(
            lambda z: (
                z["ref-close"] - z["close"] if z["close"] < z["ref-close"] else 0
            ),
            axis=1,
        )
        data["closeup-ma"] = cm.sma(data, "closeup", N=n, M=1)
        data["closedown-ma"] = cm.sma(data, "closedown", N=n, M=1)
        data["RSI"] = (
            100 * data["closeup-ma"] / (data["closeup-ma"] + data["closedown-ma"])
        )
        data["RSI-MIDDLE"] = cm.ma(data, "RSI", n)
        data["RSI-UPPER"] = data["RSI-MIDDLE"] + param * cm.std(data, "RSI", n)
        data["RSI-LOWER"] = data["RSI-MIDDLE"] - param * cm.std(data, "RSI", n)
        data[self.name] = cm.ma(data, "RSI", m)

        data = data.drop(
            columns=[
                "ref-close",
                "closeup",
                "closedown",
                "closeup-ma",
                "closedown-ma",
                "RSI",
                "RSI-MIDDLE",
                "RSI-UPPER",
                "RSI-LOWER",
            ]
        )

        return data
