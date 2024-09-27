# -*- coding=utf-8 -*-

"""
计算因子重要提醒：
1. 注意填充空值。因子数据不能为空，否则影响后面的选币计算。
2. 注意因子可能会无穷大或无穷小（在除数为0的情况下）。此时需要额外处理，否则影响后面的选币计算。
"""

from dataclasses import dataclass
from quant_ff.filters import Filter


@dataclass
class TakerBuy(Filter):
    def signal(self, *args):
        # TakerBuy
        df = args[0]
        n = args[1][0]
        factor_name = args[2]

        df[factor_name] = (
            df["taker_buy_quote_asset_volume"].rolling(n, min_periods=1).sum()
            / df["quote_volume"].rolling(n, min_periods=1).sum()
        )

        return df

    def get_parameter(self):
        param_list = []
        n_list = [3, 5, 8, 13, 21, 34, 55, 89]
        for n in n_list:
            param_list.append([n])

        return param_list
