# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VRAMTFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        与 VR 指标（Volume Ratio）一样，只是把其中的成交量替换成了成交额
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["av"] = data.apply(
            lambda z: z["quote_volume"] if z["close"] > z["ref-close"] else 0,
            axis=1,
        )
        data["bv"] = data.apply(
            lambda z: z["quote_volume"] if z["close"] < z["ref-close"] else 0,
            axis=1,
        )
        data["cv"] = data.apply(
            lambda z: z["quote_volume"] if z["close"] == z["ref-close"] else 0,
            axis=1,
        )

        data["avs"] = cm.sum(data, "av", n)
        data["bvs"] = cm.sum(data, "bv", n)
        data["cvs"] = cm.sum(data, "cv", n)
        data[self.name] = (data["avs"] + data["cvs"] / 2) / (
            data["bvs"] + data["cvs"] / 2
        )

        data = data.drop(
            columns=[
                "ref-close",
                "av",
                "bv",
                "cv",
                "avs",
                "bvs",
                "cvs",
            ]
        )

        return data
