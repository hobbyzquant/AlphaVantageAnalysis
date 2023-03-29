import pandas as pd
  

def Get_Momentum_Indicator(priceSeries):
  # return 5 values for weekly,monthly,threeMonth,sixMonth,twelveMonth momentum
  # less than -0.75 std: strong bear, -0.75:-0.25 weak bear, -0.25:0.25 chop, 0.25-0.75 weak bull, more than 0.75 std: strong bull
  # uses rolling std for each timeframe eg weekly indicator uses weekly standard deviation
  
  weeklystd = priceSeries[:5].std() # rolling 1 week standard deviation

  weeklyAmount = (priceSeries[0] - priceSeries[5]) # price returns 1 week

  if weeklyAmount < (0.75 * (-weeklystd)):
    weeklyInd = 'Strong Bear'
  elif (0.75 * (-weeklystd)) < weeklyAmount < (0.25 * -weeklystd):
    weeklyInd = 'Weak Bear'
  elif (0.25 * -weeklystd) < weeklyAmount < (0.25 * weeklystd):
    weeklyInd = 'Chop'
  elif (0.25 * weeklystd) < weeklyAmount < (0.75 * weeklystd):
    weeklyInd = 'Weak Bull'
  elif weeklyAmount > (0.75 * weeklystd):
    weeklyInd = 'Strong Bull'
  else:
    weeklyInd = 'Error'


  monthlystd = priceSeries[:21].std() # rolling 1 month standard deviation

  monthlyAmount = (priceSeries[0] - priceSeries[21]) # price returns 1 month

  if monthlyAmount < (0.75 * (-monthlystd)):
    monthlyInd = 'Strong Bear'
  elif (0.75 * (-monthlystd)) < monthlyAmount < (0.25 * -monthlystd):
    monthlyInd = 'Weak Bear'
  elif (0.25 * -monthlystd) < monthlyAmount < (0.25 * monthlystd):
    monthlyInd = 'Chop'
  elif (0.25 * monthlystd) < monthlyAmount < (0.75 * monthlystd):
    monthlyInd = 'Weak Bull'
  elif monthlyAmount > (0.75 * monthlystd):
    monthlyInd = 'Strong Bull'
  else:
    monthlyInd = 'Error'


  threeMonthstd = priceSeries[:63].std() # rolling 3 month standard deviation

  threeMonthAmount = (priceSeries[0] - priceSeries[63]) # price returns 3 months

  if threeMonthAmount < (0.75 * (-threeMonthstd)):
    threeMonthInd = 'Strong Bear'
  elif (0.75 * (-threeMonthstd)) < threeMonthAmount < (0.25 * -threeMonthstd):
    threeMonthInd = 'Weak Bear'
  elif (0.25 * -threeMonthstd) < threeMonthAmount < (0.25 * threeMonthstd):
    threeMonthInd = 'Chop'
  elif (0.25 * threeMonthstd) < threeMonthAmount < (0.75 * threeMonthstd):
    threeMonthInd = 'Weak Bull'
  elif threeMonthAmount > (0.75 * threeMonthstd):
    threeMonthInd = 'Strong Bull'
  else:
    threeMonthInd = 'Error'
  

  sixMonthstd = priceSeries[:126].std() # rolling 6 month standard deviation

  sixMonthAmount = (priceSeries[0] - priceSeries[126]) # price returns 6 months

  if sixMonthAmount < (0.75 * (-sixMonthstd)):
    sixMonthInd = 'Strong Bear'
  elif (0.75 * (-sixMonthstd)) < sixMonthAmount < (0.25 * -sixMonthstd):
    sixMonthInd = 'Weak Bear'
  elif (0.25 * -sixMonthstd) < sixMonthAmount < (0.25 * sixMonthstd):
    sixMonthInd = 'Chop'
  elif (0.25 * sixMonthstd) < sixMonthAmount < (0.75 * sixMonthstd):
    sixMonthInd = 'Weak Bull'
  elif sixMonthAmount > (0.75 * sixMonthstd):
    sixMonthInd = 'Strong Bull'
  else:
    sixMonthInd = 'Error'



  twelveMonthstd = priceSeries[:252].std() # rolling 12 month standard deviation

  twelveMonthAmount = (priceSeries[0] - priceSeries[252]) # price returns 12 months

  if twelveMonthAmount < (0.75 * (-twelveMonthstd)):
    twelveMonthInd = 'Strong Bear'
  elif (0.75 * (-twelveMonthstd)) < twelveMonthAmount < (0.25 * -twelveMonthstd):
    twelveMonthInd = 'Weak Bear'
  elif (0.25 * -twelveMonthstd) < twelveMonthAmount < (0.25 * twelveMonthstd):
    twelveMonthInd = 'Chop'
  elif (0.25 * twelveMonthstd) < twelveMonthAmount < (0.75 * twelveMonthstd):
    twelveMonthInd = 'Weak Bull'
  elif twelveMonthAmount > (0.75 * twelveMonthstd):
    twelveMonthInd = 'Strong Bull'
  else:
    twelveMonthInd = 'Error'

  return [weeklyInd, monthlyInd, threeMonthInd, sixMonthInd, twelveMonthInd]


# loop through tickers and save indicators to dataframe

def Momentum_To_DF(pricedataframe):
  # return dataframe with momo indicators

  momodf = pd.DataFrame(columns = ['Ticker','weekly','monthly','3m','6m','12m'])
  cols = pricedataframe.columns # remove date col
  pricedataframe = pricedataframe[cols]

  for col in pricedataframe:
    row = Get_Momentum_Indicator(pricedataframe[col])
    row.insert(0,col) # TODO: change this line to below for efficiency
    # what type is the row? thought it was list but this is fragmenting the dataframe
    momodf.loc[len(momodf)] = row

  return momodf
