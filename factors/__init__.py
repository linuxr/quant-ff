# -*- coding=utf-8 -*-

from quant_ff.factors.factor import Factor
from quant_ff.factors.adosc import ADOSCFactor

all = ["Factor"]


def get_factor(name: str) -> Factor:
    match name.upper():
        case "ADOSC":
            return ADOSCFactor(name=name.upper())
        case _:
            return Factor(name=name.upper())
