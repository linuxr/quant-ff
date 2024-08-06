# -*- coding=utf-8 -*-

import common as cm

from factors import Factor
from dataclasses import dataclass


@dataclass
class DBCDFactor(Factor):
    def signal(self, *args):
        """
        乖离率离差的移动平均
        """
        data = args[0]
        n = args[1][0]
        m = args[1][1]
        t = args[1][2]
        factor_name = args[2]

        data["bias"] = 100 * (data["close"] - cm.ma(data, N=n)) / cm.ma(data, N=n)
        data["ref-bias"] = cm.ref(data, "bias", m)
        data["bias-diff"] = data["bias"] - data["ref-bias"]
        data[factor_name] = cm.sma(data, "bias-diff", t, 1)

        data = data.drop(columns=["ref-bias", "bias-diff", "bias"])

        return data
