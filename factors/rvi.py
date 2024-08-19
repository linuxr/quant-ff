# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class RVIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        计算方式与 RSI 一样，不同的是将 RSI 计算中的收盘价变化值替换为收盘价在过去一段时间的标准差
        """
        n1 = para[0]
        n2 = para[1]

        data["std"] = cm.std(data, N=n1)
        data["ref-close"] = cm.ref(data, N=1)

        data["ustd"] = data.apply(
            lambda z: z["std"] if z["close"] > z["ref-close"] else 0,
            axis=1,
        )
        data["ustd"] = cm.sum(data, "ustd", n2)
        data["dstd"] = data.apply(
            lambda z: z["std"] if z["close"] < z["ref-close"] else 0,
            axis=1,
        )
        data["dstd"] = cm.sum(data, "dstd", n2)

        data[self.name] = 100 * data["ustd"] / (data["ustd"] + data["dstd"])

        data = data.drop(
            columns=[
                "std",
                "ref-close",
                "ustd",
                "dstd",
            ]
        )

        return data
