import pandas as pd


def Get_All_Tickers(path):
    tickersdf = pd.read_csv(path)
    tickers = tickersdf['Ticker']
    tickers = list(tickers)

    return tickers

def Save_To_Csv(dataframe, path):
    dataframe.to_csv(path)