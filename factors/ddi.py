# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DDIFactor(Factor):
    def signal(self, *args):
        """
        用来比较向上波动和向下波动的比例
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["hl"] = data["high"] + data["low"]
        data["ref-h"] = cm.ref(data, "high", 1)
        data["ref-l"] = cm.ref(data, "low", 1)
        data["ref-hl"] = cm.ref(data, "hl", 1)
        data["high-abs"] = abs(data["high"] - data["ref-h"])
        data["low-abs"] = abs(data["low"] - data["ref-l"])

        data["DMZ"] = data.apply(
            lambda z: max(z["high-abs"], z["low-abs"]) if z["hl"] > z["ref-hl"] else 0,
            axis=1,
        )
        data["DMF"] = data.apply(
            lambda z: max(z["high-abs"], z["low-abs"]) if z["hl"] < z["ref-hl"] else 0,
            axis=1,
        )
        data["DIZ"] = cm.sum(data, "DMZ", n) / (
            cm.sum(data, "DMZ", n) + cm.sum(data, "DMF", n)
        )
        data["DIF"] = cm.sum(data, "DMF", n) / (
            cm.sum(data, "DMZ", n) + cm.sum(data, "DMF", n)
        )
        data[factor_name] = data["DIZ"] - data["DIF"]

        data = data.drop(
            columns=[
                "hl",
                "ref-h",
                "ref-l",
                "ref-hl",
                "high-abs",
                "low-abs",
                "DMZ",
                "DMF",
                "DIZ",
                "DIF",
            ]
        )

        return data
