# AlphaVantageDataConstructor
This repository pulls data from the Alpha Vantage API and formats it in csv format for analysis. Designed to be used as a data source in a tableau project or other data viz tooling to analyze financial markets. 

Retrieves price data & financial filings data for specified tickers and provides momentum and correlation indicators

## Usage

Clone the repo & install the dependencies in *requirements.txt* with conda:

`conda create -n ENVNAME --file requirements.txt`

Insert your API key in *main.py*. You can request a free key from Alpha Vantage [here](https://www.alphavantage.co/support/#api-key)

By default, the script pulls a list of tickers provided in *Tickers.csv* and *EquityTickers.csv* and retrieves data for price, momentum, correlation, and financial filings analysis (note that financial filings only exist for equities and not ETFs, hence the different ticker lists)

Alternatively, you can analyze different tickers by uploading a csv in the same format and pointing the functions in *main.py* to your filepath

Outputs are in csv file format:
- *correlationmatrix{#tradingdays}.csv* for correlations
- *incomestatements.csv* and *balancesheets.csv* for financial filings
- *momentumdata.csv* for momentum indicators for various timeframes. Adapted from [Goulding et al (2022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3489539)
- *pricedata.csv* for price data

To produce these output csv files, ensure you have the required libraries installed and run *main.py*

## Other notes

The script has timing delays built in to comply with Alpha Vantage's API rate limits. It pulls data for 5 tickers per minute, printing to console each ticker as it goes. This means the script takes some time to run. You can read more in the [Alpha Vantage documentation](https://www.alphavantage.co/documentation/)

## Output Formats
Ouputs are saved to */AlphaVantageData* directory

***correlationmatrix.csv***
|         | AAPL | META| GOOG |...|
|---------|---------|---------|---------|-|
| **AAPL** |    1     |     0.68    |   0.97      |...|
| **META** |     0.68    |    1     |     0.84    |...|
| **GOOG**|     0.97    |     0.84    |     1    |...|
| ...|     ...   |     ...    |     ...    |...|

***momentumdata.csv***
|   Ticker  |   weekly       |   monthly      |   3m           |   6m           |   12m          |
|-----------|----------------|----------------|----------------|----------------|----------------|
|   AAPL    |   Strong Bull  |   Strong Bull  |   Strong Bull  |   Strong Bull  |   Strong Bear  |
|   MSFT    |   Weak Bull    |   Strong Bull  |   Strong Bull  |   Strong Bull  |   Strong Bear  |
|   META    |   Strong Bull  |   Strong Bull  |   Strong Bull  |   Strong Bull  |   Chop         |
|   AMZN    |   Weak Bear    |   Strong Bull  |   Strong Bull  |   Strong Bear  |   Strong Bear  |
| ...       | ...            | ...            | ...            | ...            | ...            |

***balancesheets.csv***
|   | fiscalDateEnding | totalCurrentAssets | cashAndCashEquivalentsAtCarryingValue | Ticker |...|
|---|------------------|--------------------|---------------------------------------|--------|-|
| 0 | 2022-09-30       | 30000000           | 4000000                               | AAPL   |...|
| 1 | 2022-06-30       | 28000000           | 3000000                               | AAPL   |...|
| 2 | 2022-03-31       | 32000000           | 3000000                               | AAPL   |...|
| 3 | 2022-09-30       | 10000000           | 300000                                | META   |...|
| ... | ...       | ...         | ...                               | ...   |...|

***incomestatements.csv***
|   | fiscalDateEnding | grossProfit | totalRevenue | Ticker | ... |
|---|------------------|-------------|--------------|--------|-----|
| 0 | 2022-09-30       | 30000000    | 4000000      | AAPL   | ... |
| 1 | 2022-06-30       | 28000000    | 3000000      | AAPL   | ... |
| 2 | 2022-03-31       | 32000000    | 3000000      | AAPL   | ... |
| 3 | 2022-09-30       | 10000000    | 300000       | META   | ... |
|   | ...              | ...         | ...          | ...    | ... |

***pricedata.csv***
|               |   AAPL    |   MSFT    |   META    |   AMZN    | ... |
|---------------|-----------|-----------|-----------|-----------|-----|
|   2023-03-24  |   160.25  |   280.57  |   206.01  |   98.13   | ... |
|   2023-03-23  |   158.93  |   277.66  |   204.28  |   98.71   | ... |
|   2023-03-22  |   157.83  |   272.29  |   199.81  |   98.7    | ... |
|   2023-03-21  |   159.28  |   273.78  |   202.16  |   100.61  | ... |
| ...           | ...       | ...       | ...       | ...       |     |