# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class SROCVOLFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 ROCVOL 类似，
        但是会先对成交量进行移动平均平滑处理之后再取其变化率
        """
        n = para[0]
        m = para[1]

        data["emap"] = cm.ema(data, "volume", n)
        data["ref-emap"] = cm.ref(data, "emap", m)
        data[self.name] = (data["emap"] - data["ref-emap"]) / data["ref-emap"]

        data = data.drop(columns=["emap", "ref-emap"])

        return data
