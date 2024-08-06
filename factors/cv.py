# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class CVFactor(Factor):
    def signal(self, *args):
        """
        衡量股价的波动，反映一段时间内最高价与最低价之差（价格变化幅度）的变化率
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["high-low"] = data["high"] - data["low"]
        data["h-l-ema"] = cm.ema(data, "high-low", n)
        data["ref-h-l-ema"] = cm.ref(data, "h-l-ema", n)
        data[factor_name] = (
            (data["h-l-ema"] - data["ref-h-l-ema"]) / data["ref-h-l-ema"] * 100
        )

        data = data.drop(columns=["high-low", "h-l-ema", "ref-h-l-ema"])

        return data
