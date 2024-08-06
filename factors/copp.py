# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class COPPFactor(Factor):
    def signal(self, *args):
        """
        用不同时间长度的价格变化率的加权移动平均值来衡量动量
        """
        data = args[0]
        n1 = args[1][0]
        n2 = args[1][1]
        m = args[1][2]
        factor_name = args[2]

        data["ref-close-n1"] = cm.ref(data, N=n1)
        data["ref-close-n2"] = cm.ref(data, N=n2)
        data["rc"] = 100 * (
            (data["close"] - data["ref-close-n1"]) / data["ref-close-n1"]
            + (data["close"] - data["ref-close-n2"]) / data["ref-close-n2"]
        )
        data[factor_name] = cm.wma(data, "rc", m)

        data = data.drop(columns=["ref-close-n1", "ref-close-n2", "rc"])

        return data
