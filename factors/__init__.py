# -*- coding=utf-8 -*-

from factors.factor import Factor
from factors.adosc import ADOSCFactor

all = ["Factor"]


def get_factor(name: str) -> Factor:
    match name.upper():
        case "ADOSC":
            return ADOSCFactor(name=name.upper())
        case _:
            return Factor(name=name.upper())
