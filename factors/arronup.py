# -*- coding=utf-8 -*-


import pandas as pd
from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class ARRONUPFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        ArronUp 为考虑的时间段内最高价出现时间与当前时间的距离占时间段长度的百分比
        """
        n = para[0]

        data["high-len"] = (
            data["high"].rolling(n).apply(lambda z: n - (z.idxmax() + 1) % 10)
        )
        data[self.name] = 100 * (n - data["high-len"]) / n

        data = data.drop(columns=["high-len"])

        return data
