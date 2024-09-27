# -*- coding=utf-8 -*-

import pandas as pd
from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class BTFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        TODO: 用来衡量不同的移动平均价间的差距
        """
        # data = args[0]
        # n = args[1][0]
        # factor_name = args[2]

        pass
