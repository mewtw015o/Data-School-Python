#Pandas Sort()
movies_df.title.sort_values()
movies_df['title'].sort_values() #same
type(movies_df.title.sort_values()) #Series
movies_df['title'].sort_values(ascending=False) #desc

#Sorting df by a series
movies_df.sort_values('title')
movies_df.sort_values('title', inplace=True)

#Sorting multiple columns
movies.sort_values(['content_rating','duration'])