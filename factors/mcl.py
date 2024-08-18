# -*- coding=utf-8 -*-

# import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class MCLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        （上涨股票个数-下跌股票个数）的 MACD 值
        TODO:
        """
        pass
