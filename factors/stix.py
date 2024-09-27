# -*- coding=utf-8 -*-

# import common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class STIXFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量上涨股票个数占总个数的比例
        TODO:
        """
        pass
