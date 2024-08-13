# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class AMVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用成交量作为权重对开盘价和收盘价的均值进行加权移动平均
        """
        n1 = para[0]
        n2 = para[1]

        data["amov"] = data["volume"] * (data["open"] + data["close"]) / 2

        data[f"{self.name}1"] = cm.sum(data, "amov", n1) / cm.sum(data, "volume", n1)
        data[f"{self.name}2"] = cm.sum(data, "amov", n2) / cm.sum(data, "volume", n2)

        data = data.drop(columns=["amov"])

        return data
