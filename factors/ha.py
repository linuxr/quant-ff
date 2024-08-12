# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class HAFactor(Factor):
    def signal(self, *args):
        """
        传统的蜡烛图是基于当前的最高价、最低价、开盘价和收盘价。
        而HA 蜡烛图除了考虑这些，还考虑了前一天的收盘价和 HA 开盘价

        NOTE: 与一般的指标不同，这个是重新绘制 K线图
        """
        data = args[0]
        # n = args[1][0]
        # param = args[1][1]
        factor_name = args[2]

        data[f"{factor_name}-OPEN"] = cm.sma(data, 2, 1).shift()
        data[f"{factor_name}-CLOSE"] = (
            data["open"] + data["close"] + data["high"] + data["low"]
        ) / 4
        data[f"{factor_name}-HIGH"] = data.apply(
            lambda z: max(
                z["HA-OPEN"],
                z["HA-CLOSE"],
                z["high"],
                z["low"],
            )
        )
        data[f"{factor_name}-LOW"] = data.apply(
            lambda z: min(
                z["HA-OPEN"],
                z["HA-CLOSE"],
                z["high"],
                z["low"],
            )
        )

        return data
