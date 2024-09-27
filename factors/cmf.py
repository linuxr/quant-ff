# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class CMFFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用 CLV 对成交量进行加权
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["tmp"] = (
            ((data["close"] - data["low"]) - (data["high"] - data["close"]))
            * data["volume"]
            / (data["high"] - data["low"])
        )
        data[self.factor_name] = cm.sum(data, "tmp", n) / cm.sum(data, "volume", n)

        data = data.drop(columns=["tmp"])

        return data
