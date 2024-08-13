# -*- coding=utf-8 -*-


import pandas as pd
from factors import Factor
from dataclasses import dataclass


@dataclass
class ADVRFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        TODO: 上涨成交量的移动平均与下跌成交量的移动平均之比的移动平均
        """
        pass
