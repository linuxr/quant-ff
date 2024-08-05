# -*- coding=utf-8 -*-


from factors import Factor
from dataclasses import dataclass


@dataclass
class ARRONUPFactor(Factor):
    def signal(self, *args):
        """
        ArronUp 为考虑的时间段内最高价出现时间与当前时间的距离占时间段长度的百分比
        """
        data = args[0]
        n = args[1][0]
        factor_name = args[2]

        data["high-len"] = (
            data["high"].rolling(n).apply(lambda z: n - (z.idxmax() + 1) % 10)
        )
        data[factor_name] = 100 * (n - data["high-len"]) / n

        data = data.drop(columns=["high-len"])

        return data
