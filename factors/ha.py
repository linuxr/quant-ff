# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class HAFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        传统的蜡烛图是基于当前的最高价、最低价、开盘价和收盘价。
        而HA 蜡烛图除了考虑这些，还考虑了前一天的收盘价和 HA 开盘价

        NOTE: 与一般的指标不同，这个是重新绘制 K线图
        """

        data[f"{self.name}-OPEN"] = cm.sma(data, 2, 1).shift()
        data[f"{self.name}-CLOSE"] = (
            data["open"] + data["close"] + data["high"] + data["low"]
        ) / 4
        data[f"{self.name}-HIGH"] = data.apply(
            lambda z: max(
                z["HA-OPEN"],
                z["HA-CLOSE"],
                z["high"],
                z["low"],
            )
        )
        data[f"{self.name}-LOW"] = data.apply(
            lambda z: min(
                z["HA-OPEN"],
                z["HA-CLOSE"],
                z["high"],
                z["low"],
            )
        )

        return data
