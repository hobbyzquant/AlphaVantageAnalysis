from momentum import Momentum_To_DF
from correlations import Save_Correlation_Matrix
from helpers import Get_All_Tickers
from helpers import Save_To_Csv
from prices import Construct_Prices_DF
import financialfilings


API_KEY = 'YOUR_API_KEY'


# save paths
save_prices_path = './AlphaVantageData/pricedata.csv'
save_momentum_path = './AlphaVantageData/momentumdata.csv'
save_incomestatement_path = './AlphaVantageData/incomestatements.csv'
save_balancesheet_path = './AlphaVantageData/balancesheets.csv'
retrieve_tickers_path = 'Tickers.csv'
retrieve_equitytickers_path = 'EquityTickers.csv'


# retrieve tickers to analyze for price
ticker_list = Get_All_Tickers(retrieve_tickers_path)
# retrieve tickers to analyze financial filings
ticker_list_equities = Get_All_Tickers(retrieve_equitytickers_path)


# construct a dataframe for prices
pricesdf = Construct_Prices_DF(API_KEY, ticker_list)

# save csv's for price, momentum, correlation analysis
momentumdf = Momentum_To_DF(pricesdf)

Save_To_Csv(pricesdf,save_prices_path)
Save_To_Csv(momentumdf,save_momentum_path)
Save_Correlation_Matrix(pricesdf,300)
Save_Correlation_Matrix(pricesdf,150)
Save_Correlation_Matrix(pricesdf,50)
Save_Correlation_Matrix(pricesdf,20)


# save csv's for financial filings analysis
# comment below out if updated financial filings data for all tickers is not needed

# to update all tickers including existing, set update_existing = True
incomedf = financialfilings.Construct_IncomeStatement_DF(API_KEY, ticker_list_equities, 'quarterlyReports')
Save_To_Csv(incomedf,save_incomestatement_path)

balancesheetdf = financialfilings.Construct_BalanceSheets_DF(API_KEY, ticker_list_equities, 'quarterlyReports')
Save_To_Csv(balancesheetdf,save_balancesheet_path)