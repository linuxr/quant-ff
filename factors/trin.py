# -*- coding=utf-8 -*-

# import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class TRINFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        综合考虑了上涨、下跌股票的个数和成交量
        TODO:
        """
        pass
