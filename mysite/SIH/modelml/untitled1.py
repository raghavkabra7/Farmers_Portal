import numpy as np
import pandas as pd

dataset = pd.read_csv('updatedtemp.csv')
X = dataset.iloc[:,[4,7,8,23]].values
y = dataset.iloc[:,10].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NAN', strategy = 'mean', axis=0)
imputer = imputer.fit(X.values[:,2:4])
X.values[:,2:4] = imputer.transform(X.values[:,2:4])

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
labelencoder1 = LabelEncoder()
X[:, 1] = labelencoder1.fit_transform(X[:, 1])
#onehotencoder = OneHotEncoder(categorical_features = [0,1])
#X = onehotencoder.fit_transform(X).toarray()
X=np.array(list(X[:, :]), dtype=np.float)



X[np.isnan(X)] = np.median(X[~np.isnan(X)])
y[np.isnan(y)] = np.median(y[~np.isnan(y)])

np.isnan(X).any()
np.isnan(y).any()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


"""sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train,y_train)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 4, random_state = 0)
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

def evaluate(model, test_features, test_labels):
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    
    return accuracy
print('Variance score: %.2f' % regressor.score(X_test, y_pred))
base_accuracy = evaluate(regressor, X_test, y_test)

import pickle
from pickle import dump 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd
  
# Save the trained model as a pickle string. 
saved_model = pickle.dumps(regressor) 


with open("rainfallmodel.pkl", 'wb') as file:  
    pickle.dump(regressor, file)
    
dump(regressor, open('modelrandom.pkl', 'wb'))
dump(sc_X, open('scaler.pkl', 'wb'))
np.save('en.npy', labelencoder.classes_)
np.save('en1.npy', labelencoder1.classes_)





with open("model.pkl", 'rb') as file:  
    model = pickle.load(file)
    
with open("scaler.pkl", 'rb') as file:  
    scaler = pickle.load(file)
    
le = LabelEncoder()
le.classes_ = np.load('en.npy')
le1 = LabelEncoder()
le1.classes_ = np.load('en1.npy')

s=input("state")
c=input("crop")
a=input('area')
r=input('rainfall')
s=s.upper()
#c=c.upper()
a=int(a)
r=int(r)
x=[[s,c,a,r]]
x=[['BHOPAL','Arhar/Tur',1679,269.8]]
x=pd.DataFrame(x) 
x=x.values
x[:,0] = le.transform(x[:,0])
x[:,1] = le1.transform(x[:,1])
x=np.array(list(x[:, :]), dtype=np.float)
x = scaler.transform(x)
ypred123=model.predict(x)





x.info

dataset.iloc[:,0].values




x=np.array(x)

y=x[0][0]



X_test.shape
x.shape

from sklearn.pipeline import Pipeline
pipeline = Pipeline([('encoder', le), ('scaler', scaler), ('classifier', model)])

dump(pipeline, open('pipeline.pkl', 'wb'))
with open("pipeline.pkl", 'rb') as file:  
    pipeline2 = pickle.load(file)

pipeline.fit(X_train, y_train)
score = pipeline2.score(X_test, y_test)
ypred=pipeline.predict(x)
x=[[1.37615,-0.753569,-0.235472,-0.16345]]

y_pred1 = model.predict(x)
















import pickle
from pickle import dump 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd
soil={
  "Alluvial": ["Tobacco","Cotton(lint)","Rice","Wheat","Bajra","Jowar","Soyabean","Rapeseed &Mustard","Linseed"],
  "Black": "Cotton",
  "Read": "Rice",
  "Laterite": "Coconut",
  "Arid": "Maize",
  "Mountain": "Tea",
  "Desert": "Millet",
}


with open("modelrandom.pkl", 'rb') as file:  
        model = pickle.load(file)
        
with open("scaler.pkl", 'rb') as file:  
    scaler = pickle.load(file)
    
le = LabelEncoder()
le.classes_ = np.load('en.npy')
le1 = LabelEncoder()
le1.classes_ = np.load('en1.npy')

a=int(500)
r=int(17)
s="Harda"   
s=s.upper()
ypred = {}
ypred1 = {}
#ypred["tobacoo"] = "123"

p=soil["Alluvial"]
#x[0]
for i in range(len(p)):
    print(p[i])
    c=p[i]
    #c=c.upper()
    #a=int(a)
    #r=int(r)
    x=[[s,c,a,r]]
    x=pd.DataFrame(x) 
    x=x.values
    x[:,0] = le.transform(x[:,0])
    x[:,1] = le1.transform(x[:,1])
    x=np.array(list(x[:, :]), dtype=np.float)
    x = scaler.transform(x)
    ypred123=model.predict(x)
    ypred[c]=ypred123
    