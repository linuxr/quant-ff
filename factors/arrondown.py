# -*- coding=utf-8 -*-


from factors import Factor
from dataclasses import dataclass


@dataclass
class ARRONDOWNFactor(Factor):
    def signal(self, *args):
        """
        ArronDown 为考虑的时间段内最低价出现时间与当前时间的距离占时间段长度的百分比
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["low-len"] = (
            data["low"].rolling(n).apply(lambda z: n - (z.idxmin() + 1) % 10)
        )
        data[factor_name] = 100 * (n - data["low-len"]) / n

        data = data.drop(columns=["low-len"])

        return data
