# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class ATRFactor(Factor):
    def signal(self, *args):
        """
        衡量价格波动的一种指标，它并不能反映价格的走向，一般不能直接用来产生交易信号
        """
        data = args[0]
        n = args[1][0]
        m = n // 2
        factor_name = args[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["tr"] = data.apply(
            lambda z: max(
                abs(z["high"] - z["low"]),
                abs(z["high"] - z["ref-close"]),
                abs(z["low"] - z["ref-close"]),
            ),
            axis=1,
        )
        data[factor_name] = cm.sma(data, "tr", n, 1)
        data[f"{factor_name}-UPPER"] = cm.min(data, "low", m) + data[factor_name] * 3
        data[f"{factor_name}-LOWER"] = cm.max(data, "high", m) - data[factor_name] * 3

        data = data.drop(columns=["ref-close", "tr"])

        return data
