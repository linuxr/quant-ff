# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class OSCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        反映收盘价与收盘价移动平均相差的程度
        """
        n = para[0]
        m = para[1]

        data["ref-close-n"] = cm.ref(data, N=n)
        data[self.name] = data["close"] - data["ref-close-n"]
        data[f"{self.name}-MA"] = cm.ma(data, self.name, m)

        data = data.drop(columns=["ref-close-n"])

        return data
