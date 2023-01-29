import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")
df = apple.history(start="2010-01-02", end="2023-01-01")
df["Month"]=df.index.month
df["Buy"]=df["Month"].diff()
df.iloc[0, df.columns.get_loc("Buy")] = 1
df["Buy"]=df["Buy"].replace(-11, 1)
df['Buy Price'] = np.where(df['Buy'] == 1, df["Close"], 0)
df["Buy Price cum"] = df["Buy Price"].cumsum()
df["Buy cum"] = df["Buy"].cumsum()
df["Average Buy"]=df["Buy Price cum"]/df["Buy cum"]

filter_mask=df["Buy"]==1
DCA=df[filter_mask]

Yield=(df.iloc[-1, df.columns.get_loc("Close")]-df.iloc[-1, df.columns.get_loc("Average Buy")])/df.iloc[-1, df.columns.get_loc("Average Buy")]*100
print(Yield)

df["Close"].plot(label="Close Price")
DCA["Average Buy"].plot(label="DCA")
plt.title("AAPL Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
