# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class TMFFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        和 CMF 指标类似，都是用价格对成交量加权
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-close"] = cm.ref(data, N=1)
        data["high-t"] = data.apply(
            lambda z: max(z["high"], z["ref-close"]),
            axis=1,
        )
        data["low-t"] = data.apply(
            lambda z: min(z["low"], z["ref-close"]),
            axis=1,
        )
        data[self.factor_name] = (
            data["volume"]
            * (2 * data["close"] - data["high-t"] - data["low-t"])
            / (data["high-t"] - data["low-t"])
        )
        data[self.factor_name] = cm.ema(data, self.factor_name, n)
        data[self.factor_name] = data[self.factor_name] / cm.ema(data, "volume", n)

        data = data.drop(columns=["ref-close", "high-t", "low-t"])

        return data
