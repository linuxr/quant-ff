# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DZCCIFactor(Factor):
    def signal(self, *args):
        """
        根据前段时间CCI 的变化来动态地确定阈值，从而产生交易信号
        """
        data = args[0]
        n = args[1][0]
        m = args[1][1]
        param = args[1][2]
        factor_name = args[2]

        data["tp"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ma"] = cm.ma(data, "tp", n)
        data["tp-ma"] = abs(data["tp"] - data["ma"])
        data["md"] = cm.ma(data, "tp-ma", n)
        data["CCI"] = (data["tp"] - data["ma"]) / (0.015 * data["md"])
        data["CCI-MIDDLE"] = cm.ma(data, "CCI", n)
        data["CCI-UPPER"] = data["CCI-MIDDLE"] + param * cm.std(data, "CCI", n)
        data["CCI-LOWER"] = data["CCI-MIDDLE"] - param * cm.std(data, "CCI", n)
        data[factor_name] = cm.ma(data, "CCI", m)

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
