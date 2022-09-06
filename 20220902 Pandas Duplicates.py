#duplicate rows https://www.youtube.com/watch?v=ht5buXUMqkQ
## finding duplicated in the zip code column
user.zip_code.duplicated() #Return Return if it matches any data above in 'zip_code'
user.zip_code.duplicated().sum() #Counting the duplicated
users.duplicated() #comparing entire rows to the ones above
users.loc[users.duplicated(),:] #finding and displaying the duplicated
users.loc[users.duplicated(keep='first'),:] # Not Marking the first entry of a duplicated and displaying the last entry; default 
users.loc[users.duplicated(keep='last'),:] # Not Marking the last entry of a duplicated and displaying the first entry;
users.loc[users.duplicated(keep=False),:] # marking both

users.drop_duplicates(keep='first').shape # dropping 7 rows
users.drop_duplicates(keep='last').shape # dropping 7 rows
users.drop_duplicates(keep=False).shape # dropping 14 rows, 7+7

users.duplicated(subset=['age','zip_code']).sum() #considering duplicates of column age and zip_code combine
users.drop_duplicates(subset=['age','zip_code']).shape