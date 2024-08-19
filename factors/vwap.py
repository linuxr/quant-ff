# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class VWAPFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        以成交量为权重计算价格的加权平均
        """
        n = para[0]

        data["typical"] = (data["high"] + data["low"] + data["close"]) / 3
        data["mf"] = data["volume"] * data["typical"]
        data["vol-sum"] = cm.sum(data, "volume", n)
        data["mf-sum"] = cm.sum(data, "mf", n)
        data[self.name] = data["mf-sum"] / data["vol-sum"]

        data = data.drop(columns=["typical", "mf", "vol-sum", "mf-sum"])

        return data
