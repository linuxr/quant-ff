# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class DZCCIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        根据前段时间CCI 的变化来动态地确定阈值，从而产生交易信号
        """
        n = para[0]
        m = para[1]
        param = para[2]

        data["tp"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ma"] = cm.ma(data, "tp", n)
        data["tp-ma"] = abs(data["tp"] - data["ma"])
        data["md"] = cm.ma(data, "tp-ma", n)
        data["CCI"] = (data["tp"] - data["ma"]) / (0.015 * data["md"])
        data["CCI-MIDDLE"] = cm.ma(data, "CCI", n)
        data["CCI-UPPER"] = data["CCI-MIDDLE"] + param * cm.std(data, "CCI", n)
        data["CCI-LOWER"] = data["CCI-MIDDLE"] - param * cm.std(data, "CCI", n)
        data[self.name] = cm.ma(data, "CCI", m)

        data = data.drop(
            columns=[
                "tp",
                "ma",
                "tp-ma",
                "md",
                "CCI",
                "CCI-MIDDLE",
                "CCI-UPPER",
                "CCI-LOWER",
            ]
        )

        return data
