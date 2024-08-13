# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class BBIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        对不同时间长度的移动平均线取平均，
        能够综合不同移动平均线的平滑性和滞后性
        """

        data[self.name] = (
            cm.ma(data, N=3) + cm.ma(data, N=6) + cm.ma(data, N=12) + cm.ma(data, N=24)
        ) / 4

        return data
