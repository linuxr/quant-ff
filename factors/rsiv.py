# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class RSIVFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        计算方式与 RSI 相同，只是把其中的价格变化 CLOSE REF(CLOSE,1)替换成了成交量 VOLUME
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["volup"] = data.apply(
            lambda z: z["volume"] if z["close"] > z["ref-close"] else 0,
            axis=1,
        )
        data["voldown"] = data.apply(
            lambda z: z["volume"] if z["close"] < z["ref-close"] else 0,
            axis=1,
        )
        data["sumup"] = cm.sum(data, "volup", n)
        data["sumdown"] = cm.sum(data, "voldown", n)
        data[self.name] = 100 * data["sumup"] / (data["sumup"] + data["sumdown"])

        data = data.drop(
            columns=[
                "ref-close",
                "volup",
                "voldown",
                "sumup",
                "sumdown",
            ]
        )

        return data
