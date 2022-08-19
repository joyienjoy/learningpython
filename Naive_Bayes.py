from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import numpy as np
import pandas as pd

filepath = r'J:\ESDS\Training\SEM 2\staff notes\Python\Practicals_Python_ML\GroupB\Naive Bayes\golf.csv'

# Read dataset
golf_data = pd.read_csv(filepath)
golf_data.info()
# show top 5 records
print(golf_data.head())

# Map string vales for Outlook column to numbers
d = {'Sunny': 1, 'Overcast': 2, 'Rainy': 3}
golf_data.OUTLOOK = [d[item] for item in golf_data.OUTLOOK.astype(str)]

e = {'Hot': 1, 'Mild': 2, 'Cool': 3}
golf_data.TEMPERATURE = [e[item] for item in golf_data.TEMPERATURE.astype(str)]

f = {'High': 1, 'Normal': 0}
golf_data.HUMIDITY= [f[item] for item in golf_data.HUMIDITY.astype(str)]

g = {'False': 0, 'True': 1}
golf_data.WINDY = [g[item] for item in golf_data.WINDY.astype(str)] 

print(golf_data.head(10))


# Split dataset in features and target variable
feature_cols = ['OUTLOOK','TEMPERATURE','HUMIDITY','WINDY']

# Features
features = golf_data[feature_cols] 

# Target variable
label =golf_data.PLAY_GOLF 

X_train, X_test, Y_train, Y_test = train_test_split(features, label, test_size=0.3, random_state=1)

print(X_train)
print(Y_train)
print(X_test)
print(Y_test)

# Initialise Gaussian Naive Bayes i.e Build Naive Bayes model
naive_b = GaussianNB()

# Train Decision Tree Classifer
naive_b = naive_b.fit(X_train.values,Y_train)

# Test label [Overcast,Hot,Normal,False]
test_label_custom = np.array([2,1,0,0])

# Predict the response for test instance
y_pred = naive_b.predict([test_label_custom])
print(y_pred)