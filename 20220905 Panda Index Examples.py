drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()
drinks.index #row labels
drinks.columns #Index Object, not referring to the row index
drinks.shape

#Filtering
drinks[drinks.continent=='South America']
drinks.loc[23,'beer_servings'] #calling Brazil by label 23

#Set Index
drinks.set_index('country', inplace=True)
drinks.head()
drinks.loc['Brazil','beer_servings'] #Calling 'Brazil' after setting Index

drinks.index.name = None #Rename or remove index name country
drinks.head()

drinks.index.name = 'country'
drinks.reset_index(inplace=True) #Reinserting country as a column instead of being an index
drinks.head()

drinks.describe() # a dataframe type; can use index as a dataframe
drinks.describe().index
drinks.describe().columns
drinks.describe().loc['25%','beer_servings']

#Value_counts
drinks.continent.head()
drinks.continent.value_counts()
drinks.continent.value_counts().values
drinks.continent.value_counts()['Africa']

#Sort
drinks.continent.value_counts().sort_values()
drinks.continent.value_counts().sort_index()

#Index Alignment
drinks.set_index('country', inplace=True)
drinks.head()
people = pd.Series([3000000,85000], index=['Albania','Andorra'], name='population')
drinks.beer_servings * people #Multiple, aligned by index
pd.concat([drinks,people], axis=1).head() #Inserting new columns with value by concat