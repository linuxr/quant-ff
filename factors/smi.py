# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class SMIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        可以看作 KDJ 指标的变形
        """
        n1 = para[0]
        n2 = para[1]
        n3 = para[2]

        data["max-high"] = cm.max(data, "high", n1)
        data["min-low"] = cm.min(data, "low", n1)
        data["m"] = (data["max-high"] + data["min-low"]) / 2
        data["d"] = data["close"] - data["m"]
        data["ema-d"] = cm.ema(data, "d", n2)
        data["ds"] = cm.ema(data, "ema-d", n2)
        data["max-min"] = data["max-high"] - data["min-low"]
        data["dhl"] = cm.ema(data, "max-min", n2)
        data["dhl"] = cm.ema(data, "dhl", n2)
        data[self.name] = 100 * data["ds"] / data["dhl"]
        data[f"{self.name}-MA"] = cm.ma(data, self.name, n3)

        data = data.drop(
            columns=[
                "max-high",
                "min-low",
                "m",
                "d",
                "ema-d",
                "ds",
                "max-min",
                "dhl",
            ]
        )

        return data
