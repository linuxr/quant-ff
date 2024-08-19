# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ZLMACDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        是对 MACD 指标的改进，它在计算中使用 DEMA 而不是 EMA，
        可以克服 MACD 指标的滞后性问题
        """
        n1 = para[0]
        n2 = para[1]

        data["ema-c1"] = cm.ema(data, "close", n1)
        data["ema-cc1"] = cm.ema(data, "ema-c1", n1)

        data["ema-c2"] = cm.ema(data, "close", n2)
        data["ema-cc2"] = cm.ema(data, "ema-c2", n2)

        data[self.name] = (2 * data["ema-c1"] - data["ema-cc1"]) - (
            2 * data["ema-c2"] - data["ema-cc2"]
        )

        data = data.drop(
            columns=[
                "ema-c1",
                "ema-cc1",
                "ema-c2",
                "ema-cc2",
            ]
        )

        return data
