# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class HULLMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        均线的一种，相比于普通均线有着更低的延迟性
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["X"] = 2 * cm.ema(data, N=n // 2) - cm.ema(data, N=n)

        import math

        data[self.factor_name] = cm.ema(data, "X", round(math.sqrt(n)))

        data = data.drop(columns=["X"])

        return data
