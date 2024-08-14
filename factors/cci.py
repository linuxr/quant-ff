# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class CCIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量典型价格（最高价、最低价和收盘价的均值）与其一段时间的移动平均的偏离程度
        """
        n = para[0]

        data["tp"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ma"] = cm.ma(data, "tp", n)
        data["tp-ma"] = abs(data["tp"] - data["ma"])
        data["md"] = cm.ma(data, "tp-ma", n)
        data[self.name] = (data["tp"] - data["ma"]) / (0.015 * data["md"])

        data = data.drop(columns=["tp", "ma", "tp-ma", "md"])

        return data
