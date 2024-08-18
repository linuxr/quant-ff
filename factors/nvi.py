# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class NVIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        均线的一种，相比于普通均线有着更低的延迟性
        """
        n = para[0]

        data["ref-volume"] = cm.ref(data, "volume", 1)
        data["ref-close"] = cm.ref(data, "close", 1)

        data["nvi-inc"] = data.apply(
            lambda z: (
                1 + (z["close"] - z["ref-close"]) / z["close"]
                if z["volume"] < z["ref-volume"]
                else 1
            ),
            axis=1,
        )
        data.loc[0, "nvi-inc"] = 100
        data[self.name] = cm.cumprod(data, "nvi-inc")
        data[f"{self.name}-MA"] = cm.ma(data, "NVI", n)

        data = data.drop(columns=["ref-volume", "ref-close", "nvi-inc"])

        return data
