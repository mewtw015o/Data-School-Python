#Pandas - https://www.youtube.com/watch?v=P_q0tkYqvSk
## .map : Series method - transfter values of a column into different values
train['Sex_num'] = train.Sex.map({'female' : 0, 'male' :1 }) #Dummy Variables

##.apply : Series or Panda method - Applying a function to each element in a series
train['Name_length'] = train.Name.apply(len) #length of the values in Name by using the len() function; just applying the name of the function
train['Fare_ceil'] = train.Fare.apply(np.ceil) #rounding up floats in Fare column

### .apply Series
train.Name.str.split(',').head() #this would return lists of strings
def get_element(my_list, positions):
	return my_list[position]
train.Name.str.split(',').apply(get_element, positions=0).head()
#or using lambda expression
train.Name.str.split(',').apply(lambda x : x[0]).head()

### .apply DataFrame
drinks.loc[:, 'beer_servings' : 'wine_serviings'].apply(max, axis=0)  #Max of each columns; "Traveling Down"
drinks.loc[:, 'beer_servings' : 'wine_serviings'].apply(max, axis=1)  #Max of each rows; "Traveling Down"
drinks.loc[:, 'beer_servings' : 'wine_serviings'].apply(argmax, axis=1)  #Return the column name of the max

## .applymap - applying to every element in the data frame
drinks.loc[:, 'beer_servings' : 'wine_servings'].applymap(float)
drinks.loc[:, 'beer_servings' : 'wine_servings'] = drinks.loc[:, 'beer_servings' : 'wine_servings'].applymap(float) #Perminent Change