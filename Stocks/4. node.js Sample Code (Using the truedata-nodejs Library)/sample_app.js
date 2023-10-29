const { rtConnect, rtSubscribe, rtUnsubscribe, rtFeed, historical, formatTime } = require('truedata-nodejs')
const fs = require('fs')

const user = 'Your_Username'
const pwd = 'Your_Password'
const port = 8082

const symbols = ['NIFTY 50', 'NIFTY BANK', 'NIFTY-I', 'BANKNIFTY-I', 'CRUDEOIL-I', 'SILVER-I', 'RELIANCE', 'SBIN'];

rtConnect(user, pwd, symbols, port, bidask = 1, heartbeat = 1);

rtFeed.on('touchline', touchlineHandler);
rtFeed.on('tick', tickHandler);
rtFeed.on('bidask', bidaskHandler);
rtFeed.on('bar', barHandler);

function touchlineHandler(touchline){
	console.log(touchline)
}

function tickHandler(tick){
	console.log(tick)
}

function bidaskHandler(bidask){
	console.log(bidask)
}

function barHandler(bar){
	console.log(bar)
}

// historical.auth(user, pwd); // For authentication

// from = formatTime(2021, 3, 2, 9, 15) // (year, month, date, hour, minute) // hour in 24 hour format
// to = formatTime(2021, 3, 5, 9, 15) // 


// historical
// 	.getBarData('NIFTY-I', from, to ,interval = '60mins', response ='json' )
// 	.then((res) => console.log(res))
// 	.catch((err) => console.log(err));


// historical
//     .multipleSymbols (symbols, (symbol) => historical.getBarData(symbol, '2d' , '60mins'))
//     .then((resultArray) =>{ 
//         // fs.writeFileSync('resultArray.json', JSON.stringify(resultArray))
//         resultArray.forEach(d => {
//             console.log(d)
//         })
//     })
//     .catch((err) => console.log(err));


// historical.getBhavCopyStatus().then(res => console.log(res)).catch(err => console.log(err))

// historical.getBhavCopy().then(res => console.log(res)).catch(err => console.log(err))