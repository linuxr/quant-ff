# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class PMOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        是 ROC 指标的双重平滑（移动平均）版本
        """
        n1 = para[0]
        n2 = para[1]
        n3 = para[2]

        data["ref-close"] = cm.ref(data, N=1)
        data["roc"] = (data["close"] - data["ref-close"]) / data["ref-close"] * 100
        data["roc-ma"] = cm.dma(data, "roc", 2 / n1)
        data["roc-ma10"] = data["roc-ma"] * 10
        data[self.name] = cm.dma(data, "roc-ma10", 2 / n2)
        data[f"{self.name}-SIGNAL"] = cm.dma(data, self.name, 2 / (n3 + 1))

        data = data.drop(columns=["ref-close", "roc", "roc-ma", "roc-ma10"])

        return data
