stocks = pd.read_csv('http://bit.ly/smallstocks')
stocks.index #RangeIndex

# Series - Groupby
stocks.groupby('Symbol').Close.mean()
ser = stocks.groupby(['Symbol', 'Date']).Close.mean() #This turn into a Series with Multiindex
ser.index #MultiIndex

# Series to DataFrame via unstack()
ser.unstack() #Turn a multiindex series into a DataFrame

# Series to DataFrame via Pivot Table
df = stocks.pivot_table(values='Close', index='Symbol', columns='Date') #Using Pivot to get the same result
df

# Selecting from MultiIndex Series
ser.loc['AAPL']
ser.loc['AAPL','2016-10-03'] #[Level I index, Level II index]; identical to df slicing [rows, columns]
ser.loc[:,'2016-10-03'] #[All in Level I index, '2016-10-03']

# MultiIndex
stocks.set_index(['Symbol','Date'], inplace=True)
stocks.sort_index(inplace=True)
stocks.loc['AAPL']
stocks.loc[('AAPL', '2016-10-03'), :]
stocks.loc[(['AAPL','MSFT'], '2016-10-03'), :]
stocks.loc[(['AAPL','MSFT'], '2016-10-03'), 'Close']
stocks.loc[(slice(None), ['2016-10-03','2016-10-04']), :] # selecting and filtering level II index and all level I index