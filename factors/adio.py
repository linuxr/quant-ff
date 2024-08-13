# -*- coding=utf-8 -*-

import pandas as pd
from factors import Factor
from dataclasses import dataclass


@dataclass
class ADIOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        TODO: 上涨股票个数与下跌股票个数差值的移动平均
        """
        pass
