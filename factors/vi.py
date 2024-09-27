# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        可看成 ADX 指标的变形
        用当前当前高价与前一天低价和当前低价与前一天高价的差来衡量价格变化
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-close"] = cm.ref(data, N=1)
        data["tr"] = data.apply(
            lambda z: max(
                abs(z["high"] - z["low"]),
                abs(z["low"] - z["ref-close"]),
                abs(z["high"] - z["ref-close"]),
            ),
            axis=1,
        )
        data["vmpos"] = abs(data["high"] - cm.ref(data, "low", 1))
        data["vmneg"] = abs(data["low"] - cm.ref(data, "high", 1))
        data["sumpos"] = cm.sum(data, "vmpos", n)
        data["sumneg"] = cm.sum(data, "vmneg", n)
        data["trsum"] = cm.sum(data, "tr", n)

        data[f"{self.factor_name}+"] = data["sumpos"] / data["trsum"]
        data[f"{self.factor_name}-"] = data["sumneg"] / data["trsum"]

        data = data.drop(
            columns=[
                "ref-close",
                "tr",
                "vmpos",
                "vmneg",
                "sumpos",
                "sumneg",
                "trsum",
            ]
        )

        return data
