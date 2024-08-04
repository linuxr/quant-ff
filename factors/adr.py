# -*- coding=utf-8 -*-


from factors import Factor
from dataclasses import dataclass


@dataclass
class ADRFactor(Factor):
    def signal(self, *args):
        """
        TODO: 上涨股票个数与下跌股票个数之比的简单移动平均
        """
        pass
