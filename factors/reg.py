# -*- coding=utf-8 -*-

# import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class REGFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        过去的 N 天内收盘价对序列[1,2,...,N]作回归得到回归直线
        TODO: 用到机器学习，得到回归曲线
        """
        pass
