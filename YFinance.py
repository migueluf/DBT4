import yfinance as yf
import pandas as pd


class YFinance:
    def findStocks(enterprise, start, end):
        msft = yf.Ticker(enterprise)

        hist = msft.history(start= start, end=end)

        df1 = pd.DataFrame(hist)

        std = df1['Close'].std()
        print(std)

        return std

