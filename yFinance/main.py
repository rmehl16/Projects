import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

if __name__ == '__main__':
    msft = yf.Ticker("SPY")

    # get historical market data
    hist = msft.history(period="1mo")

    fig = go.Figure(data=[go.Candlestick(x=hist.index.tolist(),
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'])])

    fig.show()