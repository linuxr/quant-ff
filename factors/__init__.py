# -*- coding=utf-8 -*-

from quant_ff.factors.factor import Factor
from quant_ff.factors.adosc import ADOSCFactor
from quant_ff.factors.adtm import ADTMFactor
from quant_ff.factors.adx import ADXFactor
from quant_ff.factors.adxr import ADXRFactor
from quant_ff.factors.amv import AMVFactor
from quant_ff.factors.apz import APZFactor
from quant_ff.factors.ar import ARFactor
from quant_ff.factors.arrondown import ARRONDOWNFactor
from quant_ff.factors.arronup import ARRONUPFactor
from quant_ff.factors.asi import ASIFactor
from quant_ff.factors.atr import ATRFactor
from quant_ff.factors.aws import AWSFactor

from quant_ff.factors.bbi import BBIFactor
from quant_ff.factors.bias import BIASFactor
from quant_ff.factors.bias36 import BIAS36Factor
from quant_ff.factors.biasvol import BIASVOLFactor
from quant_ff.factors.bop import BOPFactor
from quant_ff.factors.br import BRFactor

from quant_ff.factors.cci import CCIFactor, CCIV3Factor
from quant_ff.factors.clv import CLVFactor
from quant_ff.factors.cmf import CMFFactor
from quant_ff.factors.cmo import CMOFactor
from quant_ff.factors.copp import COPPFactor
from quant_ff.factors.cr import CRFactor
from quant_ff.factors.cv import CVFactor

from quant_ff.factors.dbcd import DBCDFactor
from quant_ff.factors.dc import DCFactor
from quant_ff.factors.ddi import DDIFactor
from quant_ff.factors.dema import DEMAFactor
from quant_ff.factors.demakder import DemakderFactor
from quant_ff.factors.dma import DMAFactor
from quant_ff.factors.do import DOFactor
from quant_ff.factors.dpo import DPOFactor
from quant_ff.factors.dzcci import DZCCIFactor
from quant_ff.factors.dzrsi import DZRSIFactor

from quant_ff.factors.volume import VOLUMEFactor, VOLUMESTDFactor

all = ["Factor"]


def get_factor(name: str) -> Factor:
    match name.upper():
        case "ADOSC":
            return ADOSCFactor(name=name)
        case "ADTM":
            return ADTMFactor(name=name)
        case "ADX":
            return ADXFactor(name=name)
        case "ADXR":
            return ADXRFactor(name=name)
        case "AMV":
            return AMVFactor(name=name)
        case "APZ":
            return APZFactor(name=name)
        case "AR":
            return ARFactor(name=name)
        case "ARRONDOWN":
            return ARRONDOWNFactor(name=name)
        case "ARRONUP":
            return ARRONUPFactor(name=name)
        case "ASI":
            return ASIFactor(name=name)
        case "ATR":
            return ATRFactor(name=name)
        case "AWS":
            return AWSFactor(name=name)
        case "BBI":
            return BBIFactor(name=name)
        case "BIAS":
            return BIASFactor(name=name)
        case "BIAS36":
            return BIAS36Factor(name=name)
        case "BIASVOL":
            return BIASVOLFactor(name=name)
        case "BOP":
            return BOPFactor(name=name)
        case "BR":
            return BRFactor(name=name)
        case "CCI":
            return CCIFactor(name=name)
        case "CCIV3":
            return CCIV3Factor(name=name)
        case "CLV":
            return CLVFactor(name=name)
        case "CMF":
            return CMFFactor(name=name)
        case "CMO":
            return CMOFactor(name=name)
        case "COPP":
            return COPPFactor(name=name)
        case "CR":
            return CRFactor(name=name)
        case "CV":
            return CVFactor(name=name)
        case "DBCD":
            return DBCDFactor(name=name)
        case "DC":
            return DCFactor(name=name)
        case "DDI":
            return DDIFactor(name=name)
        case "DEMA":
            return DEMAFactor(name=name)
        case "DEMAKDER":
            return DemakderFactor(name=name)
        case "DMA":
            return DMAFactor(name=name)
        case "DO":
            return DOFactor(name=name)
        case "DPO":
            return DPOFactor(name=name)
        case "DZCCI":
            return DZCCIFactor(name=name)
        case "DZRSI":
            return DZRSIFactor(name=name)
        case "VOLUME":
            return VOLUMEFactor(name=name)
        case "VOLUMESTD":
            return VOLUMESTDFactor(name=name)
        case _:
            return Factor(name=name)
