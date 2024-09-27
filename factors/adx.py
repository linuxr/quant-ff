# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ADXFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        计算过程中的 DI+与 DI-指标用相邻两天的最高价之差与最低价之差来反映价格的变化趋势
        """
        n = para[0]

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
        data[self.name] = (
            abs(data["MDI"] - data["PDI"]) / (data["MDI"] + data["PDI"]) * 100
        )
        data[self.name] = cm.ma(data, self.name, n)

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

        return data
