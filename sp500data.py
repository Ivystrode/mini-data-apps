import streamlit as st 
import pandas as pd 
import base64 
# import matplotlib.pyplot as plt 
# import seaborn as sns
import numpy as np 
import yfinance as yf 

st.title("S&P 500 Data")
st.markdown("""
            Retrieves the list of SP 500 from wikipedia
            """)

st.sidebar.header("User input features")

# ==========Scraping sp500 data==========

@st.cache 
def load_data():
    url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url, header=0)
    df = html[0]
    unique_sectors = df['GICS Sector'].unique()
    print(unique_sectors)
    return df
