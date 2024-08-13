# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ADOSCFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        是ADL（收集派发线）指标的短期，移动平均与长期移动平均之差
        """
        n1 = para[0]
        n2 = para[1]

        data["ad"] = (
            ((data["close"] - data["low"]) - (data["high"] - data["close"]))
            * data["volume"]
            / (data["high"] - data["low"])
        )
        data["ad"] = cm.cumsum(data, "ad")
        data["ad_ema1"] = cm.ema(data, "ad", n1)
        data["ad_ema2"] = cm.ema(data, "ad", n2)
        data[self.name] = data["ad_ema1"] - data["ad_ema2"]

        data = data.drop(columns=["ad", "ad_ema1", "ad_ema2"])

        return data
