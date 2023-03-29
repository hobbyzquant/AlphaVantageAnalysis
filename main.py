from momentum import momentumToDF
from correlations import save_correlation_matrix
from helpers import Get_All_Tickers
from helpers import save_to_csv
from prices import constructPricesDF
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
pricesdf = constructPricesDF(API_KEY, ticker_list)

# save csv's for price, momentum, correlation analysis
momentumdf = momentumToDF(pricesdf)

save_to_csv(pricesdf,save_prices_path)
save_to_csv(momentumdf,save_momentum_path)
save_correlation_matrix(pricesdf,300)
save_correlation_matrix(pricesdf,150)
save_correlation_matrix(pricesdf,50)
save_correlation_matrix(pricesdf,20)


# save csv's for financial filings analysis
# comment below out if updated financial filings data for all tickers is not needed

# to update all tickers including existing, set update_existing = True
incomedf = financialfilings.constructIncomeStatementDF(API_KEY, ticker_list_equities, 'quarterlyReports')
save_to_csv(incomedf,save_incomestatement_path)

balancesheetdf = financialfilings.constructBalanceSheetsDF(API_KEY, ticker_list_equities, 'quarterlyReports')
save_to_csv(balancesheetdf,save_balancesheet_path)