import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import numpy as np
from sklearn import *
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


# Features in vehicle dataset
col_names = ['Weight','Size', 'label']

filepath = r'J:\ESDS\Training\SEM 2\staff notes\Python\Practicals_Python_ML\GroupC\Decision Tree\apples_and_oranges.csv'
# Read data
pima = pd.read_csv(filepath)
# Show top 5 records
print(pima.head())

pima['Weight'] = pd.to_numeric(pima['Weight'])
print(pima.head())


# Split dataset in features and target variable
pima1 = pima.copy()
pima1 = pima1.drop('label', axis=1)
print(pima1)
x = pima1

# Target variable
target = pima['label']
le = LabelEncoder()
target = le.fit_transform(target)
print(target)
y = target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Create Decision Tree classifer model
clf = DecisionTreeClassifier()
clf = clf.fit(X_train.values,y_train)

# test instance
test_label_custom = np.array([75,6])
y_pred = clf.predict([test_label_custom])
print(y_pred)


plt.figure(figsize=(30,30))
dec_tree = tree.plot_tree(decision_tree=clf, feature_names=pima1.columns,
                     class_names=["orange","apple"], filled= True, precision=4, rounded= True)
plt.savefig('graph.png')