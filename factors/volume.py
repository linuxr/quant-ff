# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class VOLUMEFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        n = para[0]

        n = para[0]

        data[self.name] = data["quote_volume"].rolling(n, min_periods=1).sum()
        return data


@dataclass
class VOLUMESTDFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        # VolumeStd
        n = para[0]

        data[self.name] = data["quote_volume"].rolling(n, min_periods=1).std(ddof=0)

        return data
