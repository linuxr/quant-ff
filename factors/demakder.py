# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class Demakderactor(Factor):
    def signal(self, *args):
        """
        一个在外汇交易中用到的摆荡类技术指标
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["ref-high"] = cm.ref(data, "high", 1)
        data["Demax"] = data["high"] - data["ref-high"]
        data["Demax"] = data["Demax"].apply(lambda z: z if z > 0 else 0)

        data["ref-low"] = cm.ref(data, "low", 1)
        data["Demin"] = data["ref-low"] - data["low"]
        data["Demin"] = data["Demin"].apply(lambda z: z if z > 0 else 0)
        data[factor_name] = cm.ma(data, "Demax", n) / (
            cm.ma(data, "Demax", n) + cm.ma(data, "Demin", n)
        )

        data = data.drop(columns=["ref-high", "Demax", "ref-low", "Demin"])

        return data
