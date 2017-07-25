var candle_list = [];
var counter = 0;

function lightCandle(maximum) {
    var minimum = 1;
    var maximum = maximum;
    do {
        var random_number = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
    } while (candle_list[random_number] && counter < maximum)
    
    var candle_id = "candle".concat("_", random_number.toString());
    candle_list[random_number] = candle_id;
    counter++;
    document.getElementById(candle_id).style.opacity = "1";
}

function clearCandles(maximum) {
    var maximum = maximum;
    for (var i = 1; i < maximum + 1; i++) {
        if (candle_list[i]) {
            document.getElementById(candle_list[i]).style.opacity = "0";
        }    
    }
    candle_list = [];
    counter = 0;    
}
