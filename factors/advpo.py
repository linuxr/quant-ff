# -*- coding=utf-8 -*-


import pandas as pd
from factors import Factor
from dataclasses import dataclass


@dataclass
class ADVPOFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        TODO: 可以看成
        ADVR 指标的变形，用来衡量（上涨股票成交量下跌股票成交量）占总成交量的比例
        """
        pass
