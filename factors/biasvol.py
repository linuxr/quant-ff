# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class BIASVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        BIAS 指标的成交量版本
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data[self.factor_name] = (data["volume"] - cm.ma(data, "volume", n)) / cm.ma(
            data, "volume", n
        )

        return data
