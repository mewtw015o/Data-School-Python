#Pandas Inplace
ufc.drop('City', axis=1, inplace=True).head()
ufc.dropna(how='any').shape #inplace = False to check the impact without changes in ufc df

ufo.set_index('Time', inplace=True) 
ufo = ufo.set_index('Time') #Assignment Statement instead of inplace

#inplace = False for experiment
ufo.fillna(method='bfill').tail() #inplace = False
ufo.fillna(method='ffill').tail() #inplace = False