from pandas.core.resample import f
import yfinance as yf
import csv

coins = csv.reader(open("top50_parsed.csv"))

for coin in coins:
    print(coin)

    symbol, name = coin
    
    filename = "top50_data/{}.csv".format(symbol)

    file = open(filename, 'w')
    ticker = yf.Ticker(symbol)

    dataframe = ticker.history(period="max")
    file.write(dataframe.to_csv())

file.close()
