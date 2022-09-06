movies.shape
#(1682,8)
movies.movie_id.nunique()
#(1682)
ratings.loc[ratings.movie_id == 1, :].head()

#INNER JOIN
movie_ratings = pd.merge(movies, ratings) #merge on the same name by default
pd.merge(movies, ratings, left_on='m_id', right_on='movie_id').head() #merge on different name
pd.merge(movies, ratings, left_index=True, right_on='movie_id') #merge on index = movie_id
pd.merge(A,B,how='inner')

#Outer join - include observations found in either A or B:
pd.merge(A,B,how='outer')

#LEFT JOIN
pd.merge(A,B,how='left')
new_df = pd.merge(A_df, B_df,  how='left', left_on=['A_c1','c2'], right_on = ['B_c1','c2']) #Multiple Columns

#RIGHT JOIN
pd.merge(A,B,how='right')

#MultiIndex
both = pd.merge(close, volume, left_index=True, left_index=True)