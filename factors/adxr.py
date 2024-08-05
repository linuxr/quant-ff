# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class ADXRFactor(Factor):
    def signal(self, *args):
        """
        ADX 指标与 N 天前的 ADX 指标的均值
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["ref-high"] = cm.ref(data, "high", 1)
        data["ref-low"] = cm.ref(data, "low", 1)
        data["max-high"] = data.apply(
            lambda z: (z["high"] - z["ref-high"] if z["high"] > z["ref-high"] else 0),
            axis=1,
        )
        data["max-low"] = data.apply(
            lambda z: (z["ref-low"] - z["low"] if z["ref-low"] > z["low"] else 0),
            axis=1,
        )
        data["xpdm"] = data.apply(
            lambda z: (
                z["high"] - z["ref-high"] if z["max-high"] > z["max-low"] else 0
            ),
            axis=1,
        )
        data["pdm"] = cm.sum(data, "xpdm", n)

        data["xndm"] = data.apply(
            lambda z: (z["ref-low"] - z["low"] if z["max-low"] > z["max-high"] else 0),
            axis=1,
        )
        data["ndm"] = cm.sum(data, "xndm", n)

        data["tr1"] = abs(data["high"] - data["low"])
        data["tr2"] = abs(data["high"] - data["close"])
        data["tr3"] = abs(data["low"] - data["close"])
        data["tr"] = cm.max_idc(data, "tr1", "tr2", "tr3")
        data["tr"] = cm.sum(data, "tr", n)

        data["DI+"] = data["pdm"] / data["tr"]
        data["DI-"] = data["ndm"] / data["tr"]
        data["PDI"] = data["DI+"] * 100 / data["tr"]
        data["MDI"] = data["DI-"] * 100 / data["tr"]
        data["ADX"] = abs(data["MDI"] - data["PDI"]) / (data["MDI"] + data["PDI"]) * 100
        data["ADX"] = cm.ma(data, "ADX", n)

        data = data.drop(
            columns=[
                "ref-high",
                "ref-low",
                "max-high",
                "max-low",
                "xpdm",
                "pdm",
                "xndm",
                "ndm",
                "tr1",
                "tr2",
                "tr3",
                "tr",
                "DI+",
                "DI-",
                "PDI",
                "MDI",
            ]
        )

        data[factor_name] = data["ADX"] - cm.ref(data, "ADX", n)

        return data
