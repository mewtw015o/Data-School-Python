#Read data into Python
df = pd.read_table('',sep='|', header=None, names=['','',''],skiprows=None,skipfooter=None, index_col='country')
df = pd.read_table('...', sep='|', header=None, names=['',''], index_col='user_id')
df = pd.read_csv('.csv')
pd.read_csv('stocks.csv', usecols=[0,2,3], index_col=['Symbol','Date']) # defining columns to load, multiIndex

#method and attribute TIP Shift+Tab inside a function() for description
df.head() #method
df.head(3).drop('Time', axis=1) #display first 3 rows and all columns except Time
df.describe() #method
df.tail()
df.value_counts() #excluding Nan
df.value_counts(dropna=False)
movies.describe(include=['object'])
df.shape #attribute
df.dtypes #attribute

#Selecting Data
df['City'] #type(df['City'])
df.City #City is an attribute of the Dataframe, as a column name
df['Color Reported'] #If columns name has space, must use bracket

#Creating New columns
df['Location'] = df.City + ', ' + df.State #New columns based on exciting columns

#Select Multiple rows and columns. loc, iloc, ix (https://www.youtube.com/watch?v=xvpNA7bC8cs)
## loc
df.loc[0,:] #selecting row 0, all columns
df.loc[[0,1,2], :]
df.loc[0:2, :] #Return same as above; inclusive, *including the 2
df.loc[:, 'City']
df.loc[:,['City','State']]
df.loc[:,'City':'State'] #Between City and State columns; inclusive

df[df.City=='Oakland']
df.loc[df.City=='Oakland',:]

df[df.City=='Oakland'].State #Less efficient due to chain indexing
df.loc[df.City=='Oakland','State'] #More efficient

## iloc
df.iloc[:,[0,3]]
df.iloc[:, 0:4] #exclusive!!!; displaying first 4 columns; similiar to range()
df.iloc[0:3, :] #also, exclusive

## ix - a mix of iloc and loc
df.ix['Albania',0] #'Albania row, first column; Notes: Country names are the index
df.ix[1,'beer_servings']
df.ix['Albania': 'Andorra',0:2] # 3x2 - inclusive for string indices and exclusive for intege columns
df.ix[0:2, 0:2] #3x2 Confusing #inlusive for labels indices