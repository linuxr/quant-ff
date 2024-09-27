# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class BIAS36Factor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用来衡量不同的移动平均价间的差距
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["36"] = cm.ma(data, N=3) - cm.ma(data, N=6)
        data[self.factor_name] = cm.ma(data, "36", n)

        data = data.drop(columns=["36"])

        return data
