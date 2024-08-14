# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class HLMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        由移动平均线上下平移一定的幅度（百分比）所得
        """
        n1 = para[0]
        n2 = para[1]

        data["HMA"] = cm.ma(data, "high", N=n1)
        data["LMA"] = cm.ma(data, "low", N=n2)

        return data
