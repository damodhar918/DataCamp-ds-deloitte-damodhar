
var WebSocket = require("ws");

let user = "enter_your_user_id";
let pwd = "enter_your_password";
// enter the port you have been given for RT data. Production = 8082, Sandbox = 8084
let port = "8082"
var connection = null;
var isConnected = connect();
var url=null;
var heartbeattime = new Date(Date.now() + 3600*1000*5.5);

setInterval(socketstatus,2000);
function socketstatus()
{
     console.log(heartbeattime);
}
function connect()
{
    console.log("Connecting..");
    url = 'wss://push.truedata.in:' + port + '?user=' + user + '&password=' + pwd;
    console.log(url);
    try {
        
        connection = new WebSocket(url);
        //console.log(connection.OPEN);
                
        connection.onopen = socketonopen;
        connection.onerror = socketonerror;
        connection.onmessage = socketonmessage;
        connection.onclose = socketonclose;
        
        return true;    
    } catch (error) {
        console.log(error);
        setInterval(connect,7000);
        return false;
    }
    
}
function socketonopen(e)
{
    console.log("Connected Websocket");
}
function socketonerror(e)
{
    console.log("Websocket Error " + e.message);
    
}

function socketonmessage(e)
{
    var jsonObj = JSON.parse(e.data);
    if(jsonObj.success)
    {
        switch(jsonObj.message)
        {
            case "TrueData Real Time Data Service":
                console.log('Symbols:' + jsonObj.maxsymbols + ' Data:' +jsonObj.subscription + ' Valid Upto: ' + jsonObj.validity);
                var jsonRequest = {
                    "method":"addsymbol",
                    "symbols":["NIFTY 50","NIFTY-I","HDFC","CRUDEOIL-I","GOLD-I","SILVER-I"]
                };
                let s = JSON.stringify(jsonRequest);
                connection.send(s);
                break;
            case "symbols added":
                console.log('Added Symbols:' + jsonObj.symbolsadded);
                break;
            case "HeartBeat":
                console.log('Message ' + jsonObj.message + ' Time: ' + jsonObj.timestamp);
                break;
            default:
                console.log(jsonObj);
        }
    }
    if(jsonObj.success == false)
    {
        console.log("Not connected");
    }
    if(jsonObj.trade != null)
    {
        //console.log(jsonObj.trade)
        var tradeArray = jsonObj.trade;
        console.log("SymbolId: " + tradeArray[0] +  " Time: " + tradeArray[1] + " LTP:" + tradeArray[2] + " Volume:" + tradeArray[3]);
    }
    if(jsonObj.bidask !=null)
    {
        var bidaskArray = jsonObj.bidask;
        console.log("SymbolId: " + bidaskArray[0] +  " Time: " + bidaskArray[1] + " Bid:" + bidaskArray[2] + " BidQty:" + bidaskArray[3] + " Ask:" + bidaskArray[4] + " AskQty:" + bidaskArray[5]);
    }
    //setTimeout(closeConnection, 2000);
}

function closeConnection()
{
    connection.close();
}

function socketonclose() {
    console.log("Disconnected Websocket");
    //process.exit(0);
    
    setTimeout(connect,7000);
}
