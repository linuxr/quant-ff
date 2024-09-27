# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class BRFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量昨日收盘价在今日最高价、最低价之间的位置
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["high-refclose"] = data["high"] - data["ref-close"]
        data["refclose-low"] = data["ref-close"] - data["low"]
        data[self.name] = (
            100 * cm.sum(data, "high-refclose", n) / cm.sum(data, "refclose-low", n)
        )

        data = data.drop(
            columns=[
                "ref-close",
                "high-refclose",
                "refclose-low",
            ]
        )

        return data
