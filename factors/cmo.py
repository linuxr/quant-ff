# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class CMOFactor(Factor):
    def signal(self, *args):
        """
        用过去N天的价格上涨量和价格下跌量得到，可以看作RSI指标的变形
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["max-su"] = data.apply(
            lambda z: max(z["close"] - z["ref-close"], 0),
            axis=1,
        )
        data["max-sd"] = data.apply(
            lambda z: max(z["ref-close"] - z["close"], 0),
            axis=1,
        )
        data["su"] = cm.sum(data, "max-su", n)
        data["sd"] = cm.sum(data, "max-sd", n)
        data[factor_name] = (data["su"] - data["sd"]) / (data["su"] + data["sd"]) * 100

        data = data.drop(columns=["ref-close", "max-su", "max-sd", "su", "sd"])

        return data
