import pandas as pd


def Get_All_Tickers(path):
    tickersdf = pd.read_csv(path)
    tickers = tickersdf['Ticker']
    tickers = list(tickers)

    return tickers

def save_to_csv(dataframe, path):
    dataframe.to_csv(path)