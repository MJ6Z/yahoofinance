import pip as pip
import numpy as np

try:
    import yfinance as yf
    import pandas as pd
    import plotly.graph_objs as go
except ImportError:
    pip.main([install,'yfinance'])
    pip.main([install,'pandas'])
    pip.main([install,'plotly'])
    

while True:
    tickr = input("Company Name: ")
    try:
        data = yf.download(tickers=tickr, period='1d', interval='1m')
        break
    except:
        None


#declare figure
fig = go.Figure()

#adding data to figure, very simple as it is already beautifully organised.
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# titles
fig.update_layout(
    title=tickr+' live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

fig.show()

### to make - pass the data to Cpp file for 'analysis' (jus dumb shit)