# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class WMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        加权移动平均
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data[self.factor_name] = n * data["close"]
        for i in range(1, n):
            data[self.factor_name] = data[self.factor_name] + (n - i) * cm.ref(
                data, N=i
            )

        s = n * (n + 1) // 2
        data[self.factor_name] = data[self.factor_name] / s

        return data
