import pandas as pd

def save_correlation_matrix(pricedataframe, number_of_days):
    # save to csv the Pearson correlation coefficient of the price dataframe going back specified number of trading days

    pricedataframe = pricedataframe.iloc[:number_of_days]
    correlationsdf = pricedataframe.corr()

    save_path = './AlphaVantageData/correlationmatrix{}days.csv'.format(number_of_days)

    correlationsdf.to_csv(save_path)
