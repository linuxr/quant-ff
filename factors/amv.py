# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class AMVFactor(Factor):
    def signal(self, *args):
        """
        用成交量作为权重对开盘价和收盘价的均值进行加权移动平均
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        factor_name = args[2]

        data["amov"] = data["volume"] * (data["open"] + data["close"]) / 2

        data[f"{factor_name}1"] = cm.sum(data, "amov", n1) / cm.sum(data, "volume", n1)
        data[f"{factor_name}2"] = cm.sum(data, "amov", n2) / cm.sum(data, "volume", n2)

        data = data.drop(columns=["amov"])

        return data
