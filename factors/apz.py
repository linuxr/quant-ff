# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class APZFactor(Factor):
    def signal(self, *args):
        """
        根据价格波动性围绕均线而制成的价格通道
        """
        data = args[0]
        n = args[1][0]
        m = args[1][1]
        param = args[1][2]
        factor_name = args[2]

        data["high-low"] = data["high"] - data["low"]
        data["ema-high-low"] = cm.ema(data, "high-low", n)
        data["vol"] = cm.ema(data, "ema-high-low", n)

        data["ema-close"] = cm.ema(data, "close", m)
        data[f"{factor_name}-UPPER"] = (
            cm.ema(data, "ema-close", m) + param * data["vol"]
        )
        data[f"{factor_name}-LOWER"] = (
            cm.ema(data, "ema-close", m) - param * data["vol"]
        )

        data = data.drop(
            columns=[
                "high-low",
                "ema-high-low",
                "vol",
                "ema-close",
            ]
        )

        return data
