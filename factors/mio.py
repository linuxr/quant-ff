# -*- coding=utf-8 -*-

import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class MIOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        （上涨股票个数-下跌股票个数）与总股票个数之比的 MACD值
        TODO:
        """
        pass
