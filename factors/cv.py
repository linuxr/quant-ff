# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class CVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量股价的波动，反映一段时间内最高价与最低价之差（价格变化幅度）的变化率
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["high-low"] = data["high"] - data["low"]
        data["h-l-ema"] = cm.ema(data, "high-low", n)
        data["ref-h-l-ema"] = cm.ref(data, "h-l-ema", n)
        data[self.factor_name] = (
            (data["h-l-ema"] - data["ref-h-l-ema"]) / data["ref-h-l-ema"] * 100
        )

        data = data.drop(columns=["high-low", "h-l-ema", "ref-h-l-ema"])

        return data
