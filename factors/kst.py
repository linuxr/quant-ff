# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class KSTFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        结合了不同时间长度的 ROC 指标
        """

        data["ref-close10"] = cm.ref(data, N=10)
        data["roc-ma1"] = data["close"] - data["ref-close10"]
        data["roc-ma1"] = cm.ma(data, "roc-ma1", 10)

        data["ref-close15"] = cm.ref(data, N=15)
        data["roc-ma2"] = data["close"] - data["ref-close15"]
        data["roc-ma2"] = cm.ma(data, "roc-ma2", 10)

        data["ref-close20"] = cm.ref(data, N=20)
        data["roc-ma3"] = data["close"] - data["ref-close20"]
        data["roc-ma3"] = cm.ma(data, "roc-ma3", 10)

        data["ref-close30"] = cm.ref(data, N=30)
        data["roc-ma4"] = data["close"] - data["ref-close30"]
        data["roc-ma4"] = cm.ma(data, "roc-ma4", 10)

        data["kst-ind"] = (
            data["roc-ma1"]
            + data["roc-ma2"] * 2
            + data["roc-ma3"] * 3
            + data["roc-ma4"] * 4
        )
        data[self.name] = cm.ma(data, "kst-ind", 9)

        data = data.drop(
            columns=[
                "ref-close10",
                "ref-close15",
                "ref-close20",
                "ref-close30",
                "roc-ma1",
                "roc-ma2",
                "roc-ma3",
                "roc-ma4",
                "kst-ind",
            ]
        )

        return data
