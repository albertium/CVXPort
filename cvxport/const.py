"""
Rule: should choose name that is more informative (but less efficient to transmit)
and choose value that is less informative but shorter in format
"""
from enum import Enum


class JobError(Exception):
    pass


class Freq(Enum):
    """
    Values are frequency string
    """
    MONTHLY = 'month'
    DAILY = '1D'
    HOURLY = '1H'
    MINUTE = '1min'
    MINUTE5 = '5min'
    SECOND = '1S'
    SECOND5 = '5S'
    SECOND10 = '10S'
    TICK = 'tick'  # for testing only. We don't have the infra to trade on tick


# make sure name and value are the same since we use them interchangeably
class AssetClass(Enum):
    FX = 'FX'
    STK = 'STK'  # stock


# make sure name and value are the same since we use them interchangeably
class Broker(Enum):
    MOCK = 'MOCK'  # for testing purpose
    IB = 'IB'
    DWX = 'DWX'  # Darwinex


class CCode(Enum):
    """
    Code for controller
    """
    Succeeded = 0
    AlreadyRegistered = -1
    MissingRequiredPort = -2
    NotInRegistry = -3
    UnknownRequest = -4
    UnKnownBroker = -5
    ServerNotOnline = -6
    MissingDataServerInfo = -7
    MissingName = -8


class DCode(Enum):
    """
    Code for data server
    """
    Succeeded = 0
