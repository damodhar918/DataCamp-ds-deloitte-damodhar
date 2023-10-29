# TrueData Real Time API - Sample code
# for create_connectin you need to pip install websocket and pip install websocket-client

from websocket import create_connection

realtime_port = 8084  # 8082 for production & 8084 for sandbox environment during trial

username = 'wssand039'
password = 'santhosh039'

print("\nCreating a connection with the server...\n")

ws = ''
try:
    ws = create_connection(f"wss://push.truedata.in:{realtime_port}?user={username}&password={password}")
    print("Sending 'Connection  Request'... for desired symbols ... ")
    print(ws.recv())
    print("Connection Established !\n")
    print("Adding Symbols, Now...\n")


    ws.send('{"method": "addsymbol", "symbols":["NIFTY 50","NIFTY BANK","MCXCOMPDEX","AARTIIND",'
            '"BRITANNIA","COLPAL","DMART","EICHERMOT","GILLETTE","HDFCBANK","ICICIBANK","JKTYRE","KAJARIACER",'
            '"LICHSGFIN","MINDTREE","OFSS","PNB","QUICKHEAL","RELIANCE","SBIN","TCS","UJJIVAN","WIPRO","YESBANK",'
            '"ZEEL","NIFTY-I","BANKNIFTY-I","UPL-I","VEDL-I",'
            '"VOLTAS-I","ZEEL-I","CRUDEOIL-I","GOLDM-I","SILVERM-I","COPPER-I", "SILVER-I"]}')


    while True:
        result = ws.recv()
        print("Received '%s'" % result)

except ConnectionError as error:
    print(error)
    ws.close()
    exit()
