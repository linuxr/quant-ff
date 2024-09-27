# -*- coding=utf-8 -*-


import pandas as pd
from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class CVIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        TODO: 用来衡量不同的移动平均价间的差距
        """
        # n = para[0]

        pass
