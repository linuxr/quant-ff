# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class RSIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        反映一段时间内平均收益与平均亏损的对比
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-close"] = cm.ref(data, N=1)
        data["closeup"] = data.apply(
            lambda z: (
                z["close"] - z["ref-close"] if z["close"] > z["ref-close"] else 0
            ),
            axis=1,
        )
        data["closedown"] = data.apply(
            lambda z: (
                z["ref-close"] - z["close"] if z["close"] < z["ref-close"] else 0
            ),
            axis=1,
        )
        data["closeup-ma"] = cm.sma(data, "closeup", N=n, M=1)
        data["closedown-ma"] = cm.sma(data, "closedown", N=n, M=1)
        data[self.factor_name] = (
            100 * data["closeup-ma"] / (data["closeup-ma"] + data["closedown-ma"])
        )

        data = data.drop(
            columns=[
                "ref-close",
                "closeup",
                "closedown",
                "closeup-ma",
                "closedown-ma",
            ]
        )

        return data
