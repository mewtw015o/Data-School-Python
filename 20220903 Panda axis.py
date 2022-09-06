#axis

## Use in dropping rows and columns
### Dropping the contient column - axis = 1
drinks.drop('contient', axis=1).head() #Inplace = False; df not changed

### Dropping a row - axis = 0
drinks.drop(2, axis=0).head()

### mean()
drinks.mean() #default axis = 0; Ask Panda to Operate going down the rows to return means of each column
drinks.mean(axis=1) #default axis = 1; Ask Panda to Operate going right on the columns to return means of each row

drinks.mean(axis='index') # axis = 0
drinks.mean(axis='columns') # axis = 1