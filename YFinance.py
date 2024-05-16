import yfinance as yf
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import re

class YFinance:
    def findStocks(enterprise, start, end):
        msft = yf.Ticker(enterprise)

        hist = msft.history(start= start, end=end)

        df1 = pd.DataFrame(hist)

        std = df1['Close'].std()
        print(std)

        return std

#msft = yf.Ticker("ACM")
    #findStocks('ACM','2014-07-05','2014-07-11')

#hist = msft.history(start= "2014-07-05", end="2014-07-11")

#df1 = pd.DataFrame(hist)

#std = df1['Close'].std()

#print(std)