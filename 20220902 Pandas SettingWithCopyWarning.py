#SettingWithCopyWarning https://www.youtube.com/watch?v=4R4WsDJ-KVc
## Explaination - Pandas don't know the 'Get item' returning a Copy or a View; 
## Explaination movies[movies.content_rating=='NOT RATED'].content_rating = np.nan #This will display with SettingWithCopyWarning
## Explaination - movies[movies.content_rating=='NOT RATED'] : get item : returning either a Copy or a view
## Explaination - .content_rating = np.nan : set item
## Solution - use loc, which uses the single operation

## 1st Example: Finding null values and NOT Rated values. Replacing NOT RATED value with nan
movies.content_rating.isnull().sum() #Displaying 3 nan
movies[movies.content_rating.isnull()] #Nan

movies.content_rating.value_counts() #Unique values and count for each; "NOT RATED" to be replaced with Nan
import numpy as np
movies[movies.content_rating=='NOT RATED'].content_rating = np.nan #This will display with SettingWithCopyWarning
movies.content_rating.isnull().sum() # Still Displaying 3 nan

movies.loc[movies.content_rating=='NOT RATED', 'content_rating'].content_rating = np.nan #this works
movies.content_rating.isnull().sum() # 68 counts

## 2nd Example Changeing value to a subset
top_movies = movies.loc[movies.star_rating >= 9, :]
top_movies.loc[0, 'duration'] = 150 #SettingWithCopyWarning but value updated; Panda unsure top_movie is a view or a copy; Updating both movies and top_movies? 

top_movies = movies.loc[movies.star_rating >= 9, :].copy()
top_movies.loc[0, 'duration'] = 150 #Updating top movies df, but not in movies df