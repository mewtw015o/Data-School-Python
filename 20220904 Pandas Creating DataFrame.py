# Pandas Creating Dataframe
pd.DataFrame({'id': [...], 'color':[]}, columns = ['id','color'], index=['a','b','c']) #With dictionary, specify columns order with columns=, with index
pd.DataFrame([[100, 'red'],[101, 'blue'],[102, 'red']], columns=['id','color']) #Each list in the nested list is each row in the df, columns specific named with columns=

import numpy as np 
arr = np.random.rand(4,2)
pd.DataFrame(arr, columns=['one','two'])

#creating Large dummy DataFrame
pd.DataFrame({'student' : np.arange(100,110,1), 'test' : np.random.randint(60,101, 10)}) #inclusive at 100, exclusive at 110, step by 1
pd.DataFrame({'student' : np.arange(100,110,1), 'test' : np.random.randint(60,101, 10)}).set_index('student') # student to be the index column

#Series attaching to Df
s = pd.Series(['round','square'], index=['c', 'b'], name='shape')
df = pd.DataFrame([[100, 'red'],[101, 'blue'],[102, 'red']], columns=['id','color'], index=['a','b','c'])
pd.concat([df, s], axis=1) # Adding a new column, values are alisgned by index. 

	id	color	shape
a	100	red		NaN
b	101	blue	square
c	102	red		round
