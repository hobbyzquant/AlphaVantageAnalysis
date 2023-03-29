import requests
import pandas as pd
import time


def GetIncomeStatement(API_KEY, Ticker, timeframe):
  # return daily price dataframe
  url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={}&apikey={}'.format(Ticker,API_KEY)
  r = requests.get(url)
  data = r.json()

  if timeframe in data:
    df = pd.DataFrame(data[timeframe])
    df['Ticker'] = Ticker
  else:
    df = pd.DataFrame()
  

  return df


def GetBalanceSheet(API_KEY, Ticker, timeframe):
  # return daily price dataframe
  url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={}&apikey={}'.format(Ticker,API_KEY)
  r = requests.get(url)
  data = r.json()

  if timeframe in data:
    df = pd.DataFrame(data[timeframe])
    df['Ticker'] = Ticker
  else:
    df = pd.DataFrame()

  return df


def constructIncomeStatementDF(API_KEY, TickerlistEquities, timeframe):
  # take in list of tickers, return dataframe of income statements
  incomestatementdf = pd.DataFrame()
  request_count = 0


  for i in range(len(TickerlistEquities)):

    if request_count % 5 == 0 and request_count != 0:
      time.sleep(65)
    
    incomestatementdf = pd.concat([incomestatementdf, GetIncomeStatement(API_KEY, TickerlistEquities[i], timeframe)], ignore_index=True)
    print(TickerlistEquities[i], ' income statement')
    request_count += 1
    

  return incomestatementdf


def constructBalanceSheetsDF(API_KEY, TickerlistEquities, timeframe):
  # take in list of tickers, return dataframe of balance sheets

  balancesheetdf = pd.DataFrame()
  request_count = 0


  for i in range(len(TickerlistEquities)):
      
    if request_count % 5 == 0 and request_count != 0:
      time.sleep(65)
    
    balancesheetdf = pd.concat([balancesheetdf, GetBalanceSheet(API_KEY, TickerlistEquities[i], timeframe)], ignore_index=True)
    print(TickerlistEquities[i], ' balance sheet')
    request_count += 1
    
    
  return balancesheetdf


