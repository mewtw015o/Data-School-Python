#Pandas String
##String handling in the doc
df.item_name.str.upper() #Need to call the str on item_name column in df data frame
df.item_name.str.contains('Chicken')
df[df.item_name.str.contains('Chicken')] #Filtering Example
df.choice_description.str.replace('[', '').replace(']','') #chaining string handlings
df.choice_description.str.replace('[\[\]]', '')#chaining string handlings, regular expression