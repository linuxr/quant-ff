# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class DCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用 N 天最高价和 N 天最低价来构造价格变化的上轨和下轨，再取其均值作为中轨
        """
        n = para[0]

        data["UPPER"] = cm.max(data, "high", n)
        data["LOWER"] = cm.max(data, "low", n)
        data[self.name] = (data["UPPER"] + data["LOWER"]) / 2

        data = data.drop(columns=["UPPER", "LOWER"])

        return data
