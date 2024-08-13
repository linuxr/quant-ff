# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIASVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        BIAS 指标的成交量版本
        """
        n = para[0]

        data[self.name] = (data["volume"] - cm.ma(data, "volume", n)) / cm.ma(
            data, "volume", n
        )

        return data
