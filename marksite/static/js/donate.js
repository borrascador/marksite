var candleList = [];
var counter = 0;

function lightCandle(maximum) {
    var minimum = 1;
    var maximum = maximum;
    do {
        var randomNumber = 
        Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
    } while (candleList[randomNumber] && counter < maximum)
    
    var candleId = "candle".concat("_", randomNumber.toString());
    candleList[randomNumber] = candleId;
    counter++;
    document.getElementById(candleId).style.opacity = "1";
}

function clearCandles(maximum) {
    var maximum = maximum;
    for (var i = 1; i < maximum + 1; i++) {
        if (candleList[i]) {
            document.getElementById(candleList[i]).style.opacity = "0";
        }
    }
    candleList = [];
    counter = 0;
}
