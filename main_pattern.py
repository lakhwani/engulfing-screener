import csv

#----CANDLESTICK DETECTION FUNCTIONS:

def isBullish(candle):
    return float(candle['Close']) > float(candle['Open'])
    
def isBearish(candle):
    return float(candle['Open']) > float(candle['Close'])

def isBullish_Engulfing(candles, i):
    curr = candles[i]
    prev = candles[i-1]
    if (isBearish(prev) and isBullish(curr)) \
        and (float(prev['Close']) < float(curr['Open']) 
            and float(prev['Open']) > float(curr['Close'])):
        return True
    return False

def isBearish_Engulfing(candles, i):
    curr = candles[i]
    prev = candles[i-1]
    if (isBearish(curr) and isBullish(prev)) \
        and (float(curr['Close']) < float(prev['Open'])  
            and float(curr['Open']) > float(prev['Close'])):
        return True
    return False


#----CHECK BEARISH/BULLISH ENGULFING PER COIN:

top50_file = open('top50_parsed.csv')
top50_coins = csv.reader(top50_file) 

for coin in top50_coins:
    symbol, name = coin
    data_file = open("top50_data/{}.csv".format(symbol))
    data_reader = csv.DictReader(data_file)
    candles = list(data_reader)
    candles_recent = candles[-3:]
    for i in range(1, len(candles_recent)):
        if isBullish_Engulfing(candles_recent, i):
            print("BULLISH ENGULFING! -> For {}, Date: {}".format(symbol, candles_recent[i]['Date']))
        if isBearish_Engulfing(candles_recent, i):
            print("BEARISH ENGULFING! -> For {}, Date: {}".format(symbol, candles_recent[i]['Date']))
