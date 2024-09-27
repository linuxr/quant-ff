# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DMAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量快速移动平均与慢速移动平均之差
        """
        n1 = para[0]
        n2 = para[1]

        data[self.name] = cm.ma(data, N=n1) - cm.ma(data, N=n2)
        # data["AMA"] = cm.ma(data, factor_name, N=n1)

        return data
