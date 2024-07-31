# -*- coding=utf-8 -*-

from factors import Factor
from dataclasses import dataclass


@dataclass
class ADIPOFactor(Factor):
    def signal(self, *args):
        """
        TODO: （上涨股票个数-下跌股票个数）占股票总个数比例的移动平均值
        """
        pass
