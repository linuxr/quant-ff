# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ROCVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        ROC 的成交量版本
        """
        n = para[0]

        data["ref-vol-n"] = cm.ref(data, "volume", n)
        data[self.name] = (data["volume"] - data["ref-vol-n"]) / data["ref-vol-n"]

        data = data.drop(columns=["ref-vol-n"])

        return data
