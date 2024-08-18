# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class PPOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        MACD 的变化率版本
        """
        n1 = para[0]
        n2 = para[1]
        n3 = para[2]

        data["ema-close-n1"] = cm.ema(data, N=n1)
        data["ema-close-n2"] = cm.ema(data, N=n2)
        data[self.name] = (data["ema-close-n1"] - data["ema-close-n2"]) / data[
            "ema-close-n2"
        ]
        data[f"{self.name}-SIGNAL"] = cm.ema(data, self.name, n3)

        data = data.drop(columns=["ema-close-n1", "ema-close-n2"])

        return data
