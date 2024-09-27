# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class COPPFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用不同时间长度的价格变化率的加权移动平均值来衡量动量
        """
        n1 = para[0]
        n2 = para[1]
        m = para[2]

        data["ref-close-n1"] = cm.ref(data, N=n1)
        data["ref-close-n2"] = cm.ref(data, N=n2)
        data["rc"] = 100 * (
            (data["close"] - data["ref-close-n1"]) / data["ref-close-n1"]
            + (data["close"] - data["ref-close-n2"]) / data["ref-close-n2"]
        )
        data[self.name] = cm.wma(data, "rc", m)

        data = data.drop(columns=["ref-close-n1", "ref-close-n2", "rc"])

        return data
