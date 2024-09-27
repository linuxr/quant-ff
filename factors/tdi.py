# -*- coding=utf-8 -*-

# import common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class TDIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        根据 RSI 指标构造得到的技术指标
        TODO: 公式不全
        """
        pass
