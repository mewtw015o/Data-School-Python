#Pandas Remove Columns
df.drop('Colors Reported', axis=1, inplace=True) # Dropping the Colors Reported Column
df.drop(['City','State'], axis=1. inplace=True) # Dropping multiple columns

#Pandas remove rows
df.drop([0,1],axis=0, inplace=True)