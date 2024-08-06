# -*- coding=utf-8 -*-


from factors import Factor
from dataclasses import dataclass


@dataclass
class CVIFactor(Factor):
    def signal(self, *args):
        """
        TODO: 用来衡量不同的移动平均价间的差距
        """
        # data = args[0]
        # n = args[1][0]
        # factor_name = args[2]

        pass
