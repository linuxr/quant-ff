# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class FBFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        类似于布林带，都以价格的移动平均线为中轨，
        在中线上下浮动一定数值构造上下轨
        """
        n = para[0]

        data["ref-close"] = cm.ref(data, N=1)
        data["tr"] = data.apply(
            lambda z: max(
                abs(z["high"] - z["low"]),
                abs(z["high"] - z["ref-close"]),
                abs(z["low"] - z["ref-close"]),
            ),
            axis=1,
        )
        data["atr"] = cm.ma(data, "tr", n)
        data["middle"] = cm.ma(data, N=n)
        data["UPPER1"] = data["middle"] + 1.618 * data["atr"]
        data["UPPER2"] = data["middle"] + 2.618 * data["atr"]
        data["UPPER3"] = data["middle"] + 4.618 * data["atr"]
        data["LOWER1"] = data["middle"] - 1.618 * data["atr"]
        data["LOWER2"] = data["middle"] - 2.618 * data["atr"]
        data["LOWER3"] = data["middle"] - 4.618 * data["atr"]

        data = data.drop(columns=["ref-close", "tr", "atr", "middle"])

        return data
