# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class UOSFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 RSI 指标类似，可以用来反映市场的超买超卖状态
        """
        n = para[0]
        m = para[1]
        o = para[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["th"] = data.apply(
            lambda z: max(z["high"], z["ref-close"]),
            axis=1,
        )
        data["tl"] = data.apply(
            lambda z: min(z["low"], z["ref-close"]),
            axis=1,
        )
        data["tr"] = data["th"] - data["tl"]
        data["xr"] = data["close"] - data["tl"]
        data["xrm"] = cm.sum(data, "xr", m) / cm.sum(data, "tr", m)
        data["xrn"] = cm.sum(data, "xr", n) / cm.sum(data, "tr", n)
        data["xro"] = cm.sum(data, "xr", o) / cm.sum(data, "tr", o)
        data[self.name] = (
            100
            * (data["xrm"] * n * o + data["xrn"] * m * o + data["xro"] * m * n)
            / (m * n + m * o + n * o)
        )

        data = data.drop(
            columns=[
                "ref-close",
                "th",
                "tl",
                "tr",
                "xr",
                "xrm",
                "xrn",
                "xro",
            ]
        )

        return data
