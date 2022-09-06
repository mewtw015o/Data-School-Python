#Rename Columns https://www.youtube.com/watch?v=0uBirYFhizE
ufo.columns
ufo.rename(columns = {'Current Column Name':'New Column Name'}, inplace=True)

ufo_cols = ['city','colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols

pd.read_csv('.. .csv',names=ufo_cols, header=0) #renaming columns when loading

ufo.columns = ufc.columns.str.replace(' ', '_')