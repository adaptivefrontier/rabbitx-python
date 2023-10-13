from rabbitx_python.client.endpoints.account import AccountGroup
from rabbitx_python.client.endpoints.candle import CandleGroup, CandlePeriod
from rabbitx_python.client.endpoints.fill import FillGroup
from rabbitx_python.client.endpoints.jwt import JWTGroup
from rabbitx_python.client.endpoints.market import MarketGroup
from rabbitx_python.client.endpoints.onboarding import OnboardingGroup, APIKey
from rabbitx_python.client.endpoints.order import OrderGroup, OrderSide, OrderType, OrderStatus, TimeInForce
from rabbitx_python.client.endpoints.orderbook import OrderBookGroup
from rabbitx_python.client.endpoints.position import PositionGroup
from rabbitx_python.client.endpoints.profile import ProfileGroup
from rabbitx_python.client.endpoints.balance import BalanceGroup
from rabbitx_python.client.endpoints.trade import TradeGroup
from rabbitx_python.client.session import ClientSession
from rabbitx_python.client.websocket import WSClient, WSClientCallback


class Client(ClientSession):

    onboarding: OnboardingGroup
    orders: OrderGroup
    markets: MarketGroup
    candles: CandleGroup
    account: AccountGroup
    profile: ProfileGroup
    balance: BalanceGroup
    jwt: JWTGroup
    fills: FillGroup
    orderbook: OrderBookGroup
    trades: TradeGroup
    positions: PositionGroup

    def __init__(
        self,
        api_url: str,
        wallet: str = None,
        private_key: str = None,
        api_key: str = None,
        api_secret: str = None,
        jwt: str = None,
    ):
        super(Client, self).__init__(
            api_url,
            wallet,
            private_key,
            api_key,
            api_secret,
            jwt,
        )

        self.onboarding = OnboardingGroup(self)
        self.orders = OrderGroup(self)
        self.markets = MarketGroup(self)
        self.candles = CandleGroup(self)
        self.account = AccountGroup(self)
        self.jwt = JWTGroup(self)
        self.fills = FillGroup(self)
        self.orderbook = OrderBookGroup(self)
        self.trades = TradeGroup(self)
        self.positions = PositionGroup(self)
        self.profile = ProfileGroup(self)
        self.balance = BalanceGroup(self)
