# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class ADTMFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        通过比较开盘价往上涨的幅度和往下跌的幅度来衡量市场的人气
        """
        n = para[0]

        data["ref-open"] = cm.ref(data, "open", 1)
        data["dtm"] = data.apply(
            lambda z: (
                max(
                    z["high"] - z["open"],
                    z["open"] - z["ref-open"],
                )
                if z["open"] > z["ref-open"]
                else 0
            ),
            axis=1,
        )
        data["dbm"] = data.apply(
            lambda z: (
                max(
                    z["open"] - z["low"],
                    z["ref-open"] - z["open"],
                )
                if z["open"] < z["ref-open"]
                else 0
            ),
            axis=1,
        )
        data["stm"] = cm.sum(data, "dtm", n)
        data["sbm"] = cm.sum(data, "dbm", n)
        data["max_stm_sbm"] = data.apply(lambda d: max(d["stm"], d["sbm"]), axis=1)

        data[self.name] = (data["stm"] - data["sbm"]) / data["max_stm_sbm"]

        data = data.drop(
            columns=[
                "ref-open",
                "dtm",
                "dbm",
                "stm",
                "sbm",
                "max_stm_sbm",
            ]
        )

        return data
