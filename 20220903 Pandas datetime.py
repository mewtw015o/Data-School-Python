#dates and times in Pandas https://www.youtube.com/watch?v=yCgJGsg0Xa4
##When Time column is asof object type; also it means string type
ufo.Time.str.slice(-5,-3).astype(int).head()
ufo['Time'] = pd.to_datetime(ufo.Time) #converting from object to datetime64;
ufo.Time.dt.hour
ufo.Time.dt.weekday_name
ufo.Time.dt.dayofyear

ts = pd.to_datetime('1/1/1999') #Timestamp type; using for comparison
ufo.loc[ufo.Time >= ts, :].head()

(ufo.Time.max() - ufo.Time.min()).days #Timedelta object

#Plotting 
%matplot inline
ufo['Year'] = ufo.Time.dt.year
ufo.Year.value_counts().sort_index().plot()