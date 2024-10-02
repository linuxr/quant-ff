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

from quant_ff.factors.emv import EMVFactor
from quant_ff.factors.env import ENVFactor
from quant_ff.factors.er import ERFactor
from quant_ff.factors.expma import EXPMAFactor

from quant_ff.factors.fb import FBFactor
from quant_ff.factors.fi import FIFactor
from quant_ff.factors.fisher import FISHERFactor

from quant_ff.factors.ha import HAFactor
from quant_ff.factors.hlma import HLMAFactor
from quant_ff.factors.hma import HMAFactor
from quant_ff.factors.hullma import HULLMAFactor

from quant_ff.factors.ic import ICFactor
from quant_ff.factors.imi import IMIFactor

from quant_ff.factors.kama import KAMAFactor
from quant_ff.factors.kc import KCFactor
from quant_ff.factors.kdj import KDJFactor
from quant_ff.factors.kdjd import KDJDFactor
from quant_ff.factors.ko import KOFactor
from quant_ff.factors.kst import KSTFactor

from quant_ff.factors.lma import LMAFactor

from quant_ff.factors.ma import MAFactor
from quant_ff.factors.maamt import MAAMTFactor
from quant_ff.factors.macd import MACDFactor
from quant_ff.factors.macdvol import MACDVOLFactor
from quant_ff.factors.madisplaced import MADisplacedFactor
from quant_ff.factors.mcl import MCLFactor
from quant_ff.factors.mfi import MFIFactor
from quant_ff.factors.micd import MICDFactor
from quant_ff.factors.mio import MIOFactor
from quant_ff.factors.mtm import MTMFactor

from quant_ff.factors.nvi import NVIFactor

from quant_ff.factors.obv import OBVFactor
from quant_ff.factors.osc import OSCFactor

from quant_ff.factors.pac import PACFactor
from quant_ff.factors.pmo import PMOFactor
from quant_ff.factors.po import POFactor
from quant_ff.factors.pos import POSFactor
from quant_ff.factors.ppo import PPOFactor
from quant_ff.factors.psy import PSYFactor
from quant_ff.factors.pvi import PVIFactor
from quant_ff.factors.pvo import PVOFactor
from quant_ff.factors.pvt import PVTFactor

from quant_ff.factors.qstick import QsitckFactor

from quant_ff.factors.rccd import RCCDFactor
from quant_ff.factors.reg import REGFactor
from quant_ff.factors.rmi import RMIFactor
from quant_ff.factors.roc import ROCFactor
from quant_ff.factors.rocvol import ROCVOLFactor
from quant_ff.factors.rsi import RSIFactor
from quant_ff.factors.rsih import RSIHFactor
from quant_ff.factors.rsis import RSISFactor
from quant_ff.factors.rsiv import RSIVFactor
from quant_ff.factors.rvi import RVIFactor
from quant_ff.factors.rwi import RWIFactor

from quant_ff.factors.si import SIFactor
from quant_ff.factors.skdj import SKDJFactor
from quant_ff.factors.smi import SMIFactor
from quant_ff.factors.sroc import SROCFactor
from quant_ff.factors.srocvol import SROCVOLFactor
from quant_ff.factors.stc import STCFactor
from quant_ff.factors.stix import STIXFactor

from quant_ff.factors.t3 import T3Factor
from quant_ff.factors.tdi import TDIFactor
from quant_ff.factors.tema import TEMAFactor
from quant_ff.factors.tii import TIIFactor
from quant_ff.factors.tma import TMAFactor
from quant_ff.factors.tmf import TMFFactor
from quant_ff.factors.trin import TRINFactor
from quant_ff.factors.trix import TRIXFactor
from quant_ff.factors.tsi import TSIFactor
from quant_ff.factors.typ import TYPFactor

from quant_ff.factors.uos import UOSFactor

from quant_ff.factors.vao import VAOFactor
from quant_ff.factors.vi import VIFactor
from quant_ff.factors.vidya import VIDYAFactor
from quant_ff.factors.vma import VMAFactor
from quant_ff.factors.volume import VOLUMEFactor, VOLUMESTDFactor
from quant_ff.factors.vr import VRFactor
from quant_ff.factors.vramt import VRAMTFactor
from quant_ff.factors.vwap import VWAPFactor

from quant_ff.factors.wad import WADFactor
from quant_ff.factors.wc import WCFactor
from quant_ff.factors.wma import WMAFactor
from quant_ff.factors.wr import WRFactor
from quant_ff.factors.wvad import WVADFactor

from quant_ff.factors.zlmacd import ZLMACDFactor


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
        case "EMV":
            return EMVFactor(name=name)
        case "ENV":
            return ENVFactor(name=name)
        case "ER":
            return ERFactor(name=name)
        case "EXPMA":
            return EXPMAFactor(name=name)
        case "FB":
            return FBFactor(name=name)
        case "FI":
            return FIFactor(name=name)
        case "FISHER":
            return FISHERFactor(name=name)
        case "HA":
            return HAFactor(name=name)
        case "HLMA":
            return HLMAFactor(name=name)
        case "HMA":
            return HMAFactor(name=name)
        case "HULLMA":
            return HULLMAFactor(name=name)
        case "IC":
            return ICFactor(name=name)
        case "IMI":
            return IMIFactor(name=name)
        case "KAMA":
            return KAMAFactor(name=name)
        case "KC":
            return KCFactor(name=name)
        case "KDJ":
            return KDJFactor(name=name)
        case "KDJD":
            return KDJDFactor(name=name)
        case "KO":
            return KOFactor(name=name)
        case "KST":
            return KSTFactor(name=name)
        case "LMA":
            return LMAFactor(name=name)
        case "MA":
            return MAFactor(name=name)
        case "MAAMT":
            return MAAMTFactor(name=name)
        case "MACD":
            return MACDFactor(name=name)
        case "MACDVOL":
            return MACDVOLFactor(name=name)
        case "MADISPLACED":
            return MADisplacedFactor(name=name)
        case "MCL":
            return MCLFactor(name=name)
        case "MFI":
            return MFIFactor(name=name)
        case "MICD":
            return MICDFactor(name=name)
        case "MIO":
            return MIOFactor(name=name)
        case "MTM":
            return MTMFactor(name=name)
        case "NVI":
            return NVIFactor(name=name)
        case "OBV":
            return OBVFactor(name=name)
        case "OSC":
            return OSCFactor(name=name)
        case "PAC":
            return PACFactor(name=name)
        case "PMO":
            return PMOFactor(name=name)
        case "PO":
            return POFactor(name=name)
        case "POS":
            return POSFactor(name=name)
        case "PPO":
            return PPOFactor(name=name)
        case "PSY":
            return PSYFactor(name=name)
        case "PVI":
            return PVIFactor(name=name)
        case "PVO":
            return PVOFactor(name=name)
        case "PVT":
            return PVTFactor(name=name)
        case "QSITCK":
            return QsitckFactor(name=name)
        case "RCCD":
            return RCCDFactor(name=name)
        case "REG":
            return REGFactor(name=name)
        case "RMI":
            return RMIFactor(name=name)
        case "ROC":
            return ROCFactor(name=name)
        case "ROCVOL":
            return ROCVOLFactor(name=name)
        case "RSI":
            return RSIFactor(name=name)
        case "RSIH":
            return RSIHFactor(name=name)
        case "RSIS":
            return RSISFactor(name=name)
        case "RSIV":
            return RSIVFactor(name=name)
        case "RVI":
            return RVIFactor(name=name)
        case "RWI":
            return RWIFactor(name=name)
        case "SI":
            return SIFactor(name=name)
        case "SKDJ":
            return SKDJFactor(name=name)
        case "SMI":
            return SMIFactor(name=name)
        case "SROC":
            return SROCFactor(name=name)
        case "SROCVOL":
            return SROCVOLFactor(name=name)
        case "STC":
            return STCFactor(name=name)
        case "STIX":
            return STIXFactor(name=name)
        case "T3":
            return T3Factor(name=name)
        case "TDI":
            return TDIFactor(name=name)
        case "TEMA":
            return TEMAFactor(name=name)
        case "TII":
            return TIIFactor(name=name)
        case "TMA":
            return TMAFactor(name=name)
        case "TMF":
            return TMFFactor(name=name)
        case "TRIN":
            return TRINFactor(name=name)
        case "TRIX":
            return TRIXFactor(name=name)
        case "TSI":
            return TSIFactor(name=name)
        case "TYP":
            return TYPFactor(name=name)
        case "UOS":
            return UOSFactor(name=name)
        case "VAO":
            return VAOFactor(name=name)
        case "VI":
            return VIFactor(name=name)
        case "VIDYA":
            return VIDYAFactor(name=name)
        case "VMA":
            return VMAFactor(name=name)
        case "VOLUME":
            return VOLUMEFactor(name=name)
        case "VOLUMESTD":
            return VOLUMESTDFactor(name=name)
        case "VR":
            return VRFactor(name=name)
        case "VRAMT":
            return VRAMTFactor(name=name)
        case "VWAP":
            return VWAPFactor(name=name)
        case "WAD":
            return WADFactor(name=name)
        case "WC":
            return WCFactor(name=name)
        case "WMA":
            return WMAFactor(name=name)
        case "WR":
            return WRFactor(name=name)
        case "WVAD":
            return WVADFactor(name=name)
        case "ZLMACD":
            return ZLMACDFactor(name=name)
        case _:
            return Factor(name=name)
