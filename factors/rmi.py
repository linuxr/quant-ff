# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class RMIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 RSI 的计算方式类似，
        将 RSI 中的动量与前一天价格之差CLOSE-REF(CLOSE,1)项改为了与前四天价格之差 CLOSE-REF(CLOSE,4)
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["sma1"] = cm.ref(data, N=4)
        data["sma1"] = data.apply(
            lambda z: max(z["close"] - z["sma1"], 0),
            axis=1,
        )

        data["sma2"] = cm.ref(data, N=1)
        data["sma2"] = abs(data["close"] - data["sma2"])
        data[self.factor_name] = (
            cm.sma(data, "sma1", n, 1) / cm.sma(data, "sma2", n, 1) * 100
        )

        data = data.drop(columns=["sma1", "sma2"])

        return data
