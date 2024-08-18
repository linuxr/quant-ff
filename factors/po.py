# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class POFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        短期均线与长期均线之间的变化率
        """

        data["ema-short"] = cm.ema(data, N=9)
        data["ema-long"] = cm.ema(data, N=26)
        data[self.name] = (
            (data["ema-short"] - data["ema-long"]) / data["ema-long"] * 100
        )

        data = data.drop(columns=["ema-short", "ema-long"])

        return data
