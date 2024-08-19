# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class QsitckFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        通过比较收盘价与开盘价来反映股价趋势的方向和强度
        """
        n = para[0]

        data["close-open"] = data["close"] - data["open"]
        data[self.name] = cm.ma(data, "close-open", n)

        data = data.drop(columns=["close-open"])

        return data
