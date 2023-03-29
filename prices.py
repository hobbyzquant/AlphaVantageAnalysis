import pandas as pd
import requests
import time


def Get_Daily_Close_Prices(API_KEY, Ticker):
    # return daily price dataframe
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}'.format(Ticker,API_KEY)
    r = requests.get(url)
    data = r.json()

    if 'Time Series (Daily)' in data:
        df = pd.DataFrame(data['Time Series (Daily)']).T['5. adjusted close'].astype('float64')

    else:
        df = pd.DataFrame()
    print(Ticker, ' prices request')
    return df


# construct a csv file cols are tickers, rows are dates
# for each ticker in tickerlist, add the series to the prices dataframe

def Construct_Prices_DF(API_KEY, Tickerlist):
    # take in list of tickers, return dataframe of prices
    pricedf = pd.DataFrame()
    for i in range(len(Tickerlist)):
        
        # TODO: if ticker not in list, or first row is not most recent trading day, then run
        # if Tickerlist[i] not in Tickerlist or 

        if i % 5 == 0 and i != 0:
            time.sleep(65)

        pricedf[Tickerlist[i]] = Get_Daily_Close_Prices(API_KEY, Tickerlist[i])
        pricedf = pricedf.iloc[:300]
        print(Tickerlist[i], ' prices to df')

    return pricedf