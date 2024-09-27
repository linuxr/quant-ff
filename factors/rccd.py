# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class RCCDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        先对 RC 指标进行平滑处理，
        再取不同时间长度的移动平均的差值，再取移动平均
        """
        n1 = para[0]
        n2 = para[1]
        m = para[2]

        data["ref-close"] = cm.ref(data, N=m)
        data["rc"] = data["close"] / data["ref-close"]
        data["ref-rc"] = cm.ref(data, "rc", 1)
        data["arc1"] = cm.sma(data, "ref-rc", m, 1)
        data["ref-arc1"] = cm.ref(data, "arc1", 1)
        data["dif"] = cm.ma(data, "ref-arc1", n1) - cm.ma(data, "ref-arc1", n2)
        data[self.name] = cm.sma(data, "dif", m, 1)

        data = data.drop(
            columns=[
                "ref-close",
                "rc",
                "ref-rc",
                "arc1",
                "ref-arc1",
                "dif",
            ]
        )

        return data
