from truedata_ws.websocket.TD import TD
import time
import logging
from datetime import date

# tick
# username = 'your_username'
# password = 'your_password'

realtime_port = 8082

url = 'push.truedata.in'
# url = 'replay.truedata.in'

symbols = symbols = ["NIFTY 50", "NIFTY BANK", "NIFTY MID SELECT", "INDIA VIX", "MCXCOMPDEX", "AXISBANK-I", "BRITANNIA",
           "COLPAL", "DMART", "EICHERMOT", "GILLETTE", "HDFCBANK", "ICICIBANK", "PIDILITIND-I", "KAJARIACER",
           "LICHSGFIN", "MINDTREE", "PEL-I", "PNB-I", "QUICKHEAL", "RELIANCE", "SBIN", "TCS", "UJJIVAN",
           "WIPRO", "YESBANK", "ZEEL", "NIFTY-I", "BANKNIFTY-I", "FINNIFTY-1", "UPL-I", "VEDL-I", "VOLTAS-I",
           "ZEEL-I", "FINNIFTY-I", "MCXENRGDEX-I", "MCXENRGDEX-II", "MCXENRGDEX-III",
           "ZINC-I", "USDINR-I", "EURUSD-I", "GBPINR-I", "EURINR-I", "GBPUSD-I", "JPYINR-I",
           "USDJPY-I", "COPPER-I", "SILVERMIC-I", "SILVERMIC-II",
           "COPPER-II", "COPPER22JULFUT", "SILVER-I", "SILVER-II", "GOLD-I", "GOLD-II", "CRUDEOIL-I",
           "CRUDEOIL-II", "BAJAJ-AUTO", "M&M", "MIDCPNIFTY-I", "NATURALGAS-I",
           "SENSEX", "RELIANCE_BSE"]


td_obj = TD(username, password, live_port=realtime_port, url=url, log_level=logging.DEBUG, log_format="%(message)s",
            historical_api=False)
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
print('\n')
print('Starting Real Time Feed.... ')

req_ids = td_obj.start_live_data(symbols)

live_data_objs = {}

time.sleep(2)

for req_id in req_ids:
    print(f'touchlinedata -> {td_obj.touchline_data[req_id]}')


@td_obj.trade_callback
def strategy_callback(symbol_id, tick_data):
    print(f'Trade  update > {tick_data}')


@td_obj.bidask_callback
def new_bidask(symbol_id, tick_data):
    print(f"BidAsk update > {tick_data}")


# Keep your thread alive
while True:
    time.sleep(120)
