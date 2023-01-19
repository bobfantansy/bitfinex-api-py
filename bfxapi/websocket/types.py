from typing import Type, Tuple, List, Dict, TypedDict, Union, Optional, Any

from dataclasses import dataclass

from ..labeler import _Type

from ..notification import Notification

JSON = Union[Dict[str, "JSON"], List["JSON"], bool, int, float, str, Type[None]]

#region Type hinting for Websocket Public Channels

@dataclass
class TradingPairTicker(_Type):
    BID: float
    BID_SIZE: float
    ASK: float
    ASK_SIZE: float
    DAILY_CHANGE: float
    DAILY_CHANGE_RELATIVE: float
    LAST_PRICE: float
    VOLUME: float
    HIGH: float
    LOW: float

@dataclass
class FundingCurrencyTicker(_Type):
    FRR: float
    BID: float
    BID_PERIOD: int
    BID_SIZE: float
    ASK: float
    ASK_PERIOD: int
    ASK_SIZE: float
    DAILY_CHANGE: float
    DAILY_CHANGE_RELATIVE: float
    LAST_PRICE: float
    VOLUME: float
    HIGH: float
    LOW: float
    FRR_AMOUNT_AVAILABLE: float

@dataclass
class TradingPairTrade(_Type):
    ID: int 
    MTS: int 
    AMOUNT: float 
    PRICE: float

@dataclass
class FundingCurrencyTrade(_Type):
    ID: int 
    MTS: int 
    AMOUNT: float 
    RATE: float 
    PERIOD: int

@dataclass
class TradingPairBook(_Type):
    PRICE: float 
    COUNT: int 
    AMOUNT: float

@dataclass
class FundingCurrencyBook(_Type):
    RATE: float 
    PERIOD: int 
    COUNT: int 
    AMOUNT: float

@dataclass    
class TradingPairRawBook(_Type):
    ORDER_ID: int
    PRICE: float 
    AMOUNT: float

@dataclass      
class FundingCurrencyRawBook(_Type):
    OFFER_ID: int 
    PERIOD: int 
    RATE: float 
    AMOUNT: float

@dataclass
class Candle(_Type):
    MTS: int
    OPEN: float
    CLOSE: float
    HIGH: float
    LOW: float
    VOLUME: float

@dataclass
class DerivativesStatus(_Type):
    TIME_MS: int
    DERIV_PRICE: float
    SPOT_PRICE: float
    INSURANCE_FUND_BALANCE: float
    NEXT_FUNDING_EVT_TIMESTAMP_MS: int
    NEXT_FUNDING_ACCRUED: float
    NEXT_FUNDING_STEP: int
    CURRENT_FUNDING: float
    MARK_PRICE: float
    OPEN_INTEREST: float
    CLAMP_MIN: float
    CLAMP_MAX: float

#endregion

#region Type hinting for Websocket Authenticated Channels
@dataclass
class Order(_Type):
    ID: int
    GID: int
    CID: int
    SYMBOL: str
    MTS_CREATE: int
    MTS_UPDATE: int
    AMOUNT: float
    AMOUNT_ORIG: float
    ORDER_TYPE: str
    TYPE_PREV: str
    MTS_TIF: int
    FLAGS: int
    ORDER_STATUS: str
    PRICE: float
    PRICE_AVG: float
    PRICE_TRAILING: float
    PRICE_AUX_LIMIT: float
    NOTIFY: int
    HIDDEN: int
    PLACED_ID: int
    ROUTING: str
    META: JSON

@dataclass
class Position(_Type):
    SYMBOL: str
    STATUS: str
    AMOUNT: float
    BASE_PRICE: float
    MARGIN_FUNDING: float
    MARGIN_FUNDING_TYPE: int
    PL: float
    PL_PERC: float
    PRICE_LIQ: float
    LEVERAGE: float
    POSITION_ID: int
    MTS_CREATE: int
    MTS_UPDATE: int
    TYPE: int
    COLLATERAL: float
    COLLATERAL_MIN: float
    META: JSON

@dataclass
class TradeExecuted(_Type):
    ID: int 
    SYMBOL: str 
    MTS_CREATE: int
    ORDER_ID: int 
    EXEC_AMOUNT: float 
    EXEC_PRICE: float 
    ORDER_TYPE: str 
    ORDER_PRICE: float 
    MAKER:int
    CID: int

@dataclass
class TradeExecutionUpdate(_Type):
    ID: int 
    SYMBOL: str 
    MTS_CREATE: int
    ORDER_ID: int 
    EXEC_AMOUNT: float 
    EXEC_PRICE: float 
    ORDER_TYPE: str 
    ORDER_PRICE: float 
    MAKER:int
    FEE: float
    FEE_CURRENCY: str
    CID: int

@dataclass
class FundingOffer(_Type):
    ID: int
    SYMBOL: str
    MTS_CREATED: int
    MTS_UPDATED: int
    AMOUNT: float
    AMOUNT_ORIG: float
    OFFER_TYPE: str
    FLAGS: int
    STATUS: str
    RATE: float
    PERIOD: int
    NOTIFY: int
    HIDDEN: int
    RENEW: int

@dataclass
class FundingCredit(_Type):
    ID: int
    SYMBOL: str
    SIDE: int
    MTS_CREATE: int
    MTS_UPDATE: int
    AMOUNT: float
    FLAGS: int
    STATUS: str
    RATE: float
    PERIOD: int
    MTS_OPENING: int
    MTS_LAST_PAYOUT: int
    NOTIFY: int
    HIDDEN: int
    RENEW: int
    RATE_REAL: float
    NO_CLOSE: int
    POSITION_PAIR: str

@dataclass
class FundingLoan(_Type):
    ID: int
    SYMBOL: str
    SIDE: int
    MTS_CREATE: int
    MTS_UPDATE: int
    AMOUNT: float
    FLAGS: int
    STATUS: str
    RATE: float
    PERIOD: int
    MTS_OPENING: int
    MTS_LAST_PAYOUT: int
    NOTIFY: int
    HIDDEN: int
    RENEW: int
    RATE_REAL: float
    NO_CLOSE: int

@dataclass
class Wallet(_Type):
    WALLET_TYPE: str
    CURRENCY: str
    BALANCE: float
    UNSETTLED_INTEREST: float
    BALANCE_AVAILABLE: float
    DESCRIPTION: str
    META: JSON

@dataclass
class BalanceInfo(_Type):
    AUM: float
    AUM_NET: float

#endregion