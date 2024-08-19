# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class TIIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        计算方式与 RSI 相同，只是把其中的前后两天价格变化替换为价格与均线的差值
        """
        n1 = para[0]
        n2 = para[1]
        m = (n1 // 2) + 1

        data["dev"] = data["close"] - cm.ma(data, N=n1)
        data["devpos"] = data["dev"].apply(lambda z: z if z > 0 else 0)
        data["devneg"] = data["dev"].apply(lambda z: -1 * z if z < 0 else 0)
        data["sumpos"] = cm.sum(data, "devpos", m)
        data["sumneg"] = cm.sum(data, "devneg", m)
        data[self.name] = 100 * data["sumpos"] / (data["sumpos"] + data["sumneg"])
        data[f"{self.name}-SIGNAL"] = cm.ema(data, self.name, n2)

        data = data.drop(columns=["dev", "devpos", "devneg", "sumpos", "sumneg"])

        return data
