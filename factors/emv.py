# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class EMVFactor(Factor):
    def signal(self, *args):
        """
        综合考虑了成交量和价格（中间价）的变化
        """
        data = args[0]
        # n = args[1][0]
        factor_name = args[2]

        VOLUME_DIVISOR = 1000000

        data["ref-high"] = cm.ref(data, "high", 1)
        data["ref-low"] = cm.ref(data, "low", 1)
        data["mid-pt-move"] = (data["high"] - data["low"]) / 2 - (
            data["ref-high"] - data["ref-low"]
        ) / 2
        data["box-ratio"] = (
            data["volume"] / VOLUME_DIVISOR / (data["high"] - data["low"])
        )

        data[factor_name] = data["mid-pt-move"] / data["box-ratio"]

        data = data.drop(
            columns=[
                "ref-high",
                "ref-low",
                "mid-pt-move",
                "box-ratio",
            ]
        )

        return data
