# -*- coding=utf-8 -*-

import common as cm
import numpy as np

from factors import Factor
from dataclasses import dataclass


@dataclass
class KAMAFactor(Factor):
    def signal(self, *args):
        """
        与 VIDYA 指标类似
        不同的是，KAMA 指标可以设置权值的上界 FAST 和下界 SLOW
        """
        data = args[0]
        n = args[1][0]
        n1 = args[1][1]
        n2 = args[1][2]
        factor_name = args[2]

        data["direction"] = data["close"] - cm.ref(data, N=n)
        data["volatility"] = abs(data["close"] - cm.ref(data, N=1))
        data["volatility"] = cm.sum(data, "volatility", N=n)
        data["er"] = data["direction"] / data["volatility"]
        fast = 2 / (n1 + 1)
        slow = 2 / (n2 + 1)
        data["smooth"] = data["er"] * (fast - slow) + slow
        data["cof"] = data["smooth"] * data["smooth"]

        data[factor_name] = data["cof"] * data["close"]

        data = data.reset_index()
        for idx, row in data[1:].iterrows():
            cof = row["cof"]
            kama = data.loc[idx - 1, factor_name]

            if not np.isnan(cof) and not np.isnan(kama):
                data.loc[idx, factor_name] = row[factor_name] + (1 - cof) * kama

        data = data.drop(columns=["direction", "volatility", "er", "smooth", "cof"])

        return data
