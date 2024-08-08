# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DZRSIFactor(Factor):
    def signal(self, *args):
        """
        动态的 RSI，原理与 DZCCI 相同，计算公式为 DZCCI 中的CCI 替换为 RSI
        """
        data = args[0]
        n = args[1][0]
        m = args[1][1]
        param = args[1][2]
        factor_name = args[2]

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
        data[factor_name] = cm.ma(data, "RSI", m)

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
