# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VIDYAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        均线的一种，不同的是，VIDYA 的权值加入了 ER（EfficiencyRatio）指标
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-close"] = cm.ref(data, N=1)
        data["abs-close"] = abs(data["close"] - data["ref-close"])
        data["VI"] = abs(data["close"] - cm.ref(data, N=n)) / cm.sum(
            data, "abs-close", n
        )
        data[self.factor_name] = (
            data["VI"] * data["close"] + (1 - data["VI"]) * data["ref-close"]
        )

        data = data.drop(columns=["ref-close", "abs-close", "VI"])

        return data
