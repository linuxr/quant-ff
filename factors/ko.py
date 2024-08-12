# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class KOFactor(Factor):
    def signal(self, *args):
        """
        目的是为了观察短期和长期股票资金的流入和流出的情况
        它的主要用途是确认股票价格趋势的方向和强度
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        factor_name = args[2]

        data["typical"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ref-typical"] = cm.ref(data, "typical", 1)
        data["volume"] = data.apply(
            lambda z: (
                z["volume"]
                if (z["typical"] - z["ref-typical"]) >= 0
                else -1 * z["volume"]
            ),
            axis=1,
        )
        data["volume-ema1"] = cm.ema(data, "volume", n1)
        data["volume-ema2"] = cm.ema(data, "volume", n2)
        data[factor_name] = data["volume-ema1"] - data["volume-ema2"]

        data = data.drop(
            columns=[
                "typical",
                "ref-typical",
                "volume-ema1",
                "volume-ema2",
            ]
        )

        return data
