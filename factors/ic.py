# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class ICFactor(Factor):
    def signal(self, *args):
        """
        将SPAN_A 与 SPAN_B 之间的部分称为云，
        价格在云上，则说明是上涨趋势（如果 SPAN_A>SPAN_B，则上涨趋势强烈；否则上涨趋势较弱）；
        价格在云下，则为下跌趋势（如果SPAN_A<SPAN_B，则下跌趋势强烈；否则下跌趋势较弱）
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        n3 = args[1][2]
        # factor_name = args[2]

        data["TS"] = (cm.max(data, "high", n1) + cm.min(data, "low", n1)) / 2
        data["KS"] = (cm.max(data, "high", n2) + cm.min(data, "low", n2)) / 2
        data["SPAN-A"] = (data["TS"] + data["KS"]) / 2
        data["SPAN-B"] = (cm.max(data, "high", n3) + cm.min(data, "low", n3)) / 2

        return data
