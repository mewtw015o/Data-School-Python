#Groupby https://www.youtube.com/watch?v=qy0fDqoMJx8
df.beer_servings.mean()
df.[df.contient=='Africa'].beer_servings.mean()
df.groupby('contient').beer_servings.mean()
df.groupby('contient').beer_servings.min()
df.groupby('contient').beer_servings.max()
df.groupby('contient').beer_servings.agg(['count','min','max','mean'])
drinks.groupby('continent').mean() #For all numeric columns
%matplotlib inline
drinks.groupby('continent').mean().plot(kind='bar')

#Filter rows by column values
is_long = movies.duration >= 200
movies[is_long]

movies[movies.duration >= 200] #inner part creates a series of a boolean
movies[movies.duration >= 200].genre
movies[movies.duration >= 200]['genre']
movies.loc[movies.duration >= 200, 'genre']

#Multiple Filter criteria 
(movies.duration >= 200) and (movies.genre == 'Drama') # returning a series of boolean
movies[(movies.duration >= 200) and (movies.genre == 'Drama')] #Evaluation Order
movies[(movies.duration >= 200) | (movies.genre == 'Drama')] #Evaluation Order
movies.genre.isin(['Crime','Drama', 'Action'])

#Missing Values in Pandas https://www.youtube.com/watch?v=fCMrO_VzeL8
ufo.isnull().tail()
ufo.notnull().tail()
ufo.isnull().sum() # Return numbers of Missing values in each columns
ufo.isnull().sum(axis=1) # Return numbers of Missing values in each row
ufo[ufo.City.isnull()] #rows that City is missing
ufo.dropna(how='any').shape #drop any rows that contains nan in any columns
ufo.dropna(how='any', inplace=True).shape #drop any rows that contains nan in any columns
ufo.dropna(how='all').shape
ufo.dropna(subset=['City','Shape Reported'], how='any').shape #drop a row if any nan values in City and Shape Reported columns
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
ufo.fillna(method='bfill').tail() #inplace = False
ufo.fillna(method='ffill').tail() #inplace = False
