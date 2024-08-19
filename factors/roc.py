# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ROCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量价格的涨跌幅
        """

        data["ref-close-100"] = cm.ref(data, N=100)
        data[self.name] = (data["close"] - data["ref-close-100"]) / data[
            "ref-close-100"
        ]

        data = data.drop(columns=["ref-close-100"])

        return data
