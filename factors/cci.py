# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class CCIFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        衡量典型价格（最高价、最低价和收盘价的均值）与其一段时间的移动平均的偏离程度
        """
        n = para[0]

        data["tp"] = (data["high"] + data["low"] + data["close"]) / 3
        data["ma"] = cm.ma(data, "tp", n)
        data["tp-ma"] = abs(data["tp"] - data["ma"])
        data["md"] = cm.ma(data, "tp-ma", n)
        data[self.name] = (data["tp"] - data["ma"]) / (0.015 * data["md"])

        data = data.drop(columns=["tp", "ma", "tp-ma", "md"])

        return data


@dataclass
class CCIV3Factor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        # Cci因子魔改的第三个版本，参考自《中性5期船队因子库》: https://bbs.quantclass.cn/thread/13472
        n = para[0]

        oma = data["open"].ewm(span=n, adjust=False).mean()
        hma = data["high"].ewm(span=n, adjust=False).mean()
        lma = data["low"].ewm(span=n, adjust=False).mean()
        cma = data["close"].ewm(span=n, adjust=False).mean()
        tp = (oma + hma + lma + cma) / 4
        ma = tp.ewm(span=n, adjust=False).mean()
        md = (cma - ma).abs().ewm(span=n, adjust=False).mean()
        data[self.name] = (tp - ma) / md

        return data
