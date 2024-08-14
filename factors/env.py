# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ENVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        由移动平均线上下平移一定的幅度（百分比）所得
        """
        n = para[0]
        param = para[1]

        data["mac"] = cm.ma(data, N=n)
        data[f"{self.name}-UPPER"] = data["mac"] * (1 + param)
        data[f"{self.name}-LOWER"] = data["mac"] * (1 - param)

        data = data.drop(columns=["mac"])

        return data
