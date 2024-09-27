# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ATRFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量价格波动的一种指标，它并不能反映价格的走向，一般不能直接用来产生交易信号
        """
        n = para[0]
        m = n // 2

        data["ref-close"] = cm.ref(data, N=1)
        data["tr"] = data.apply(
            lambda z: max(
                abs(z["high"] - z["low"]),
                abs(z["high"] - z["ref-close"]),
                abs(z["low"] - z["ref-close"]),
            ),
            axis=1,
        )
        data[self.name] = cm.sma(data, "tr", n, 1)
        data[f"{self.name}-UPPER"] = cm.min(data, "low", m) + data[self.name] * 3
        data[f"{self.name}-LOWER"] = cm.max(data, "high", m) - data[self.name] * 3

        data = data.drop(columns=["ref-close", "tr"])

        return data
