# -*- coding=utf-8 -*-

import pandas as pd
from pathlib import Path


def read_file(fp):
    """
    读取csv文件和zip文件
    """
    data = pd.DataFrame()
    p = Path(fp)

    if not p.exists():
        print("[ERROR] 文件 {} 不存在".format(fp))
        return data

    ext = p.suffix
    if ext == ".csv":
        data = pd.read_csv(p)

    if ext == ".zip":
        data = pd.read_csv(p, compression="zip")

    return data


def ref(data: pd.DataFrame, col="close", N=10):
    """
    N 天前的值，比如 ref(data, CLOSE, 10) 为 10 天前的收盘价
    """
    return data[col].shift(N)


def sum(data: pd.DataFrame, col="close", N=10):
    """
    过去 N 天 col 列的和
    比如，sum(成交量, 10)
    """
    return data[col].rolling(N).sum()


def cumsum(data: pd.DataFrame, col="close"):
    """
    列 col 的累积和
    """
    return data[col].cumsum()


def cumprod(data: pd.DataFrame, col="close"):
    """
    列 col 的累积连乘
    """
    return data[col].cumprod()


def max(data: pd.DataFrame, col="close", N=10):
    """
    过去 N 天 col 列的最大值
    """
    return data[col].rolling(N).max()


def min(data: pd.DataFrame, col="close", N=10):
    """
    过去 N 天 col 列的最小值
    """
    return data[col].rolling(N).min()


def std(data: pd.DataFrame, col="close", N=10):
    """
    过去 N 天 col 列的标准值
    """
    return data[col].rolling(N).std()


def max_col(data: pd.DataFrame, *cols):
    """
    最大值
    """
    return data.loc[:, cols].max(axis=1)


def min_col(data: pd.DataFrame, *cols):
    """
    最小值
    """
    return data.loc[:, cols].min(axis=1)


def ma(data: pd.DataFrame, col="close", N=10):
    """
    移动平均线，过去 N 天 col 列的平均值
    """
    return data[col].rolling(N).mean()


def ema(data: pd.DataFrame, col="close", N=10):
    """
    指数移动平均线
    EMA=2/(N+1)* X+(N-1)/(N+1)*REF(EMA,1)
    """
    return data[col].ewm(span=N, adjust=True).mean()


def sma(data: pd.DataFrame, col="close", N=10, M=3):
    """
    简单移动平均线
    SMA=M/N*X+(N-M)/N*REF(SMA,1)
    """
    return data[col].ewm(span=(N - M), adjust=True).mean()


def wma(data: pd.DataFrame, col="close", N=10):
    """
    加权移动平均线
    WMA=(N*X+(N-1)*REF(X,1)+...+1*REF(X,N-1))/(N+1)*N/2)
    """
    data = data[col].rolling(N)
    return data.apply(lambda x: x[::-1].cumsum().sum() * 2 / N / (N - 1))


def dma(data: pd.DataFrame, col="close", a=10):
    """
    动态移动平均线
    DMA=a*X+(1-a)*REF(X,1)
    """
    return data[col] * a + (1 - a) * data[col].shift(1)
