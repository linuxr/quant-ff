# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ROCVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        ROC 的成交量版本
        """
        n = para[0]
        self.factor_name = f"{self.name}_{str(para)}"

        data["ref-vol-n"] = cm.ref(data, "volume", n)
        data[self.factor_name] = (data["volume"] - data["ref-vol-n"]) / data[
            "ref-vol-n"
        ]

        data = data.drop(columns=["ref-vol-n"])

        return data
