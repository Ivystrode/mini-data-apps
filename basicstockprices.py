import streamlit as st 
import yfinance as yf 

"""
This just shows a really basic stock price plot in the browser
with streamlit run [name].py
Use markdown to style
"""

st.write("""
         # Shows stock prices
         Stock **closing price** and ***stuff***
         """)

tickerSymbol = "TSLA"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2021-5-31")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)