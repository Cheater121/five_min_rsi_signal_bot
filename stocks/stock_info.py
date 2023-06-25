from datetime import timedelta

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

from config_data.config import load_config
from errors.setup_logger import logger
from strategies.rsi import get_current_rsi

config = load_config()

TCS_TOKEN = config.tcs_client.token


class StockAnalyzer:

    def __init__(self, figi: str, ticker: str):
        self.figi = figi
        self.ticker = ticker
        self.old_levels = {"RSI": None}
        self.levels = {"RSI": None}

    def get_new_prices(self, interval=CandleInterval.CANDLE_INTERVAL_1_MIN, days=1):
        try:
            with Client(TCS_TOKEN) as client:
                close_prices = []
                for candle in client.get_all_candles(figi=self.figi, from_=now() - timedelta(days=days),
                                                     interval=interval):
                    # print(candle, "\n")
                    close_price = candle.close.units + candle.close.nano / (10 ** 9)
                    close_prices.append(close_price)
                self._update_prices(close_prices)
        except Exception as e:
            logger.exception(f"Exception in get prices method: \n{e}\n")

    def _update_prices(self, close_prices):
        try:
            rsi = get_current_rsi(close_prices)
            self.levels = {"RSI": rsi}
            print(f"{self.ticker} {self.levels}")
        except Exception as e:
            logger.exception(f"Exception in update prices method: \n{e}\n")


ozon = StockAnalyzer("BBG00Y91R9T3", "OZON")
sber = StockAnalyzer("BBG004730N88", "SBER")
sgzh = StockAnalyzer("BBG0100R9963", "SGZH")
poly = StockAnalyzer("BBG004PYF2N3", "POLY")
vkco = StockAnalyzer("BBG00178PGX3", "VKCO")
tatn = StockAnalyzer("BBG004RVFFC0", "TATN")
nvtk = StockAnalyzer("BBG00475KKY8", "NVTK")
spbe = StockAnalyzer("BBG002GHV6L9", "SPBE")
nlmk = StockAnalyzer("BBG004S681B4", "NLMK")
pikk = StockAnalyzer("BBG004S68BH6", "PIKK")
five = StockAnalyzer("BBG00JXPFBN0", "FIVE")
afks = StockAnalyzer("BBG004S68614", "AFKS")
yndx = StockAnalyzer("BBG006L8G4H1", "YNDX")
rosn = StockAnalyzer("BBG004731354", "ROSN")
alrs = StockAnalyzer("BBG004S68B31", "ALRS")
gmkn = StockAnalyzer("BBG004731489", "GMKN")
aflt = StockAnalyzer("BBG004S683W7", "AFLT")
gazp = StockAnalyzer("BBG004730RP0", "GAZP")
lkoh = StockAnalyzer("BBG004731032", "LKOH")
moex = StockAnalyzer("BBG004730JJ5", "MOEX")

stocks_list = [ozon, sber, sgzh, poly, vkco, tatn, nvtk, spbe, nlmk, pikk, five, afks, yndx, rosn, alrs, gmkn, aflt,
               gazp, lkoh, moex]
