# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DOFactor(Factor):
    def signal(self, *args):
        """
        平滑处理（双重移动平均）后的 RSI 指标
        """
        data = args[0]
        n = args[1][0]
        m = args[1][1]
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
        data["RSI-EMA"] = cm.ema(data, "RSI", n)
        data[factor_name] = cm.ema(data, "RSI-EMA", m)

        data = data.drop(
            columns=[
                "ref-close",
                "closeup",
                "closedown",
                "closeup-ma",
                "closedown-ma",
                "RSI",
                "RSI-EMA",
            ]
        )

        return data
