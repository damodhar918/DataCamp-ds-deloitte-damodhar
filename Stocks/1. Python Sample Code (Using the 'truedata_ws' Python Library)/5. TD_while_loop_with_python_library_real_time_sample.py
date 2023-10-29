# Real Time Data Sample - Using TrueData Websocket Python Library

from truedata_ws.websocket.TD import TD
from copy import deepcopy
import pandas as pd
from datetime import date
import time

username = 'wssand039'
password = 'santhosh039'

# Default production port is 8082 in the library. Other ports may be given to you during trial.
realtime_port = 8082

td_app = TD(username, password, live_port=realtime_port, historical_api=False)

symbols = ["NIFTY 50","NIFTY BANK","NIFTY20102911000CE","MCXCOMPDEX","AARTIIND","BRITANNIA",
        #    "COLPAL","DMART","EICHERMOT","GILLETTE","HDFCBANK","ICICIBANK","JKTYRE","KAJARIACER",
        #    "LICHSGFIN","MINDTREE","OFSS","PNB","QUICKHEAL","RELIANCE","SBIN","TCS","UJJIVAN",
        #    "WIPRO","YESBANK","ZEEL","NIFTY20OCTFUT", "NIFTY-I","BANKNIFTY-I","TCS20OCTFUT","RELIANCE20OCTFUT",
           "UPL-I","VEDL-I","VOLTAS-I","ZEEL-I","CRUDEOIL20OCTFUT","CRUDEOIL-I","GOLDM-I","SILVERM-I","COPPER-I", "SILVER-I"]

print('Starting Real Time Feed.... ')
print(f'Port > {realtime_port}')

req_ids = td_app.start_live_data(symbols)
live_data_objs = {}

time.sleep(1)

for req_id in req_ids:
    live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])
    print(f'touchlinedata -> {td_app.touchline_data[req_id]}')

while True:
    for req_id in req_ids:
        if not td_app.live_data[req_id] == live_data_objs[req_id]:
            print(td_app.live_data[req_id])  # your code in the previous version had a  print(td_app.live_data[req_id]).__dict__ here.
            live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])

