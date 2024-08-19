# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class TSIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        一种双重移动平均指标
        TSI 对两天收盘价的差值取移动平均
        """
        n1 = para[0]
        n2 = para[1]

        data["ref-close"] = cm.ref(data, N=1)
        data["ema-up"] = data["close"] - data["ref-close"]
        data["ema-up"] = cm.ema(data, "ema-up", n1)
        data["ema-up"] = cm.ema(data, "ema-up", n2)

        data["ema-down"] = abs(data["close"] - data["ref-close"])
        data["ema-down"] = cm.ema(data, "ema-down", n1)
        data["ema-down"] = cm.ema(data, "ema-down", n2)

        data[self.name] = data["ema-up"] / data["ema-down"] * 100

        data = data.drop(columns=["ref-close", "ema-up", "ema-down"])

        return data
