#Dummy Variables - https://www.youtube.com/watch?v=0s_1IsROgDc
train['Sex_num'] = train.Sex.map({'female' : 0, 'male' :1 })

## Female or Male; k = 2
pd.get_dummies(train.Sex)
pd.get_dummies(train.Sex).loc[:,1:] #This will drop the Female columns; Only need one dummy (k-1) when k = 2

## k = 3
pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,1:]

## Dummy with two columns
pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True)

## Insert dummies columns with concat
embarked_dummies = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,1:]
train = pd.concat([train, embarked_dummies], axis=1)
