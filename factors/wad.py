# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class WADFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        是一个筑底指标
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["trh"] = data.apply(
            lambda z: max(z["high"], z["ref-close"]),
            axis=1,
        )
        data["trl"] = data.apply(
            lambda z: min(z["low"], z["ref-close"]),
            axis=1,
        )
        data["ad"] = data.apply(
            lambda z: (
                z["close"] - z["trl"]
                if z["close"] > z["ref-close"]
                else z["close"] - z["trh"]
            ),
            axis=1,
        )
        data["ad"] = data.apply(
            lambda z: 0 if z["close"] == z["ref-close"] else z["ad"],
            axis=1,
        )
        data[self.name] = cm.cumsum(data, "ad")
        data[f"{self.name}-MA"] = cm.ma(data, self.name, n)

        data = data.drop(columns=["ref-close", "trh", "trl", "ad"])

        return data
