# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class OBVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        把成交量分为正的成交量（价格上升时的成交量）和负的成交量（价格下降时）的成交量
        """
        n1 = para[0]
        n2 = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data["vol"] = data.apply(
            lambda z: (
                z["volume"] if z["close"] > z["ref-close"] else -1 * z["volume"]
            ),
            axis=1,
        )
        data["vol"] = data.apply(
            lambda z: z["vol"] if z["close"] != z["ref-close"] else 0,
            axis=1,
        )
        data[self.name] = 0
        data[self.name] = cm.ref(data, self.name, 1)
        data[self.name] = data[self.name] + data["vol"]
        data[f"{self.name}-HISTOGRAM"] = cm.ema(data, self.name, n1) - cm.ema(
            data, self.name, n2
        )

        data = data.drop(columns=["ref-close", "vol"])

        return data
