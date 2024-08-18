# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class PVIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        成交量升高的交易日的价格变化百分比的累积
        """
        n = para[0]

        data["ref-vol"] = cm.ref(data, "volume", 1)
        data["ref-close"] = cm.ref(data, N=1)
        data["pvi-inc"] = data.apply(
            lambda z: (
                (z["close"] - z["ref-close"]) / z["close"]
                if z["volume"] > z["ref-vol"]
                else 0
            ),
            axis=1,
        )
        data[self.name] = cm.cumsum(data, "pvi-inc")
        data[f"{self.name}-MA"] = cm.ma(data, self.name, n)

        data = data.drop(columns=["ref-vol", "ref-close", "pvi-inc"])

        return data
