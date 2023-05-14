import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

if __name__ == '__main__':
    msft = yf.Ticker("MSFT")

    # get historical market data
    hist = msft.history(period="100d")

    #hist['Date'] = hist['Date'].apply(lambda x: x[:10])

    print(isinstance(hist, pd.DataFrame))

    print(hist.columns, hist.index)
    print(hist.size)
    print(hist)

    fig = go.Figure(data=[go.Candlestick(x=hist.index.tolist(),
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'])])

    fig.show()