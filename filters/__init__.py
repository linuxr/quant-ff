# -*- coding=utf-8 -*-

from quant_ff.filters.Filter import Filter
from quant_ff.filters.TakerBuy import TakerBuy
from quant_ff.filters.ZhangDieFuAbsMax import ZhangDieFuAbsMax

__all__ = ["Filter"]


def get_filter(name: str) -> Filter:
    match name.upper():
        case "TAKERBUY":
            return TakerBuy(name=name)
        case "ZHANGDIEFUABSMAX":
            return ZhangDieFuAbsMax(name=name)
        case _:
            return Filter()
