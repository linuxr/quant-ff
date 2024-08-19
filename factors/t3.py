# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class T3Factor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        三重指数平均线
        """
        n = para[0]
        va = para[1]

        data["ema-close"] = cm.ema(data, N=n)
        data["T1"] = data["ema-close"] * (1 + va) - cm.ema(data, "ema-close", n) * va

        data["ema-t1"] = cm.ema(data, "T1", n)
        data["T2"] = data["ema-t1"] * (1 + va) - cm.ema(data, "ema-t1") * va

        data["ema-t2"] = cm.ema(data, "T2", n)
        data[self.name] = data["ema-t2"] * (1 + va) - cm.ema(data, "ema-t2") * va

        data = data.drop(columns=["ema-close", "T1", "ema-t1", "T2", "ema-t2"])

        return data
