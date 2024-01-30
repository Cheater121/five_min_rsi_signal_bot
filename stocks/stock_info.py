from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
from datetime import datetime, timedelta

from errors.setup_logger import logger
from strategies.rsi import get_current_rsi
from config_data.config import load_config


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
# tatn = StockAnalyzer("BBG004RVFFC0", "TATN")
nvtk = StockAnalyzer("BBG00475KKY8", "NVTK")
spbe = StockAnalyzer("BBG002GHV6L9", "SPBE")
nlmk = StockAnalyzer("BBG004S681B4", "NLMK")
pikk = StockAnalyzer("BBG004S68BH6", "PIKK")
# five = StockAnalyzer("BBG00JXPFBN0", "FIVE")
afks = StockAnalyzer("BBG004S68614", "AFKS")
yndx = StockAnalyzer("BBG006L8G4H1", "YNDX")
rosn = StockAnalyzer("BBG004731354", "ROSN")
alrs = StockAnalyzer("BBG004S68B31", "ALRS")
gmkn = StockAnalyzer("BBG004731489", "GMKN")
aflt = StockAnalyzer("BBG004S683W7", "AFLT")
gazp = StockAnalyzer("BBG004730RP0", "GAZP")
lkoh = StockAnalyzer("BBG004731032", "LKOH")
moex = StockAnalyzer("BBG004730JJ5", "MOEX")
svav = StockAnalyzer('BBG004S68JR8', 'SVAV')
cian = StockAnalyzer('BBG012YQ6P43', 'CIAN')
fixp = StockAnalyzer('BBG00ZHCX1X2', 'FIXP')
chmf = StockAnalyzer('BBG00475K6C3', 'CHMF')
smlt = StockAnalyzer('BBG00F6NKQX3', 'SMLT')
wush = StockAnalyzer('TCS00A105EX7', 'WUSH')
vtbr = StockAnalyzer('BBG004730ZJ9', 'VTBR')
etln = StockAnalyzer('BBG001M2SC01', 'ETLN')
kmaz = StockAnalyzer('BBG000LNHHJ9', 'KMAZ')
mtss = StockAnalyzer('BBG004S681W1', 'MTSS')
bspb = StockAnalyzer('BBG000QJW156', 'BSPB')
mtlr = StockAnalyzer('BBG004S68598', 'MTLR')
rasp = StockAnalyzer('BBG004S68696', 'RASP')
geco = StockAnalyzer('TCS00A105BN4', 'GECO')
reni = StockAnalyzer('BBG00QKJSX05', 'RENI')
flot = StockAnalyzer('BBG000R04X57', 'FLOT')
rnft = StockAnalyzer('BBG00F9XX7H4', 'RNFT')
rual = StockAnalyzer('BBG008F2T3T2', 'RUAL')
irao = StockAnalyzer('BBG004S68473', 'IRAO')
fees =StockAnalyzer('BBG00475JZZ6', 'FEES')
tcsg = StockAnalyzer('BBG00QPYJ5H0', 'TCSG')
posi = StockAnalyzer('TCS00A103X66', 'POSI')
magn = StockAnalyzer('BBG004S68507', 'MAGN')
lsrg = StockAnalyzer('BBG004S68C39', 'LSRG')
sftl = StockAnalyzer('BBG0136BTL03', 'SFTL')
uwgn = StockAnalyzer('BBG008HD3V85', 'UWGN')
carm = StockAnalyzer('TCS00A105NV2', 'CARM')
astr = StockAnalyzer('RU000A106T36', 'ASTR')
eutr = StockAnalyzer('TCS00A1002V2', 'EUTR')
ugld = StockAnalyzer('TCS00A0JPP37', 'UGLD')
mgkl = StockAnalyzer('TCS00A0JVJQ8', 'MGKL')
hnfg = StockAnalyzer('TCS00A106XF2', 'HNFG')
astr = StockAnalyzer('RU000A106T36', 'ASTR')


stocks_list = [ozon, sber, sgzh, poly, vkco, nvtk, spbe, nlmk, pikk, afks, yndx, rosn, alrs, gmkn, aflt, gazp, lkoh, moex, svav, cian, fixp, chmf, smlt, wush, vtbr, etln, kmaz, mtss, bspb, mtlr, rasp, geco, reni, flot, rnft, rual, irao, fees, tcsg, posi, magn, lsrg, sftl, uwgn, carm, astr, hnfg, mgkl, ugld, eutr]
               
