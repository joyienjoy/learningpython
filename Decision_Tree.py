import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import plot_tree

# Read data and Show top 5 records
pima = pd.read_csv("diabetes.csv")
print(pima.head())

# check dataset
pima.info()
pima.isnull().any()

# visualisation
sns.pairplot(data=pima, hue='Age')
# co-relation matric
sns.heatmap(pima.corr())

# Split dataset in features and target variable
#feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
#               'DiabetesPedigreeFunction', 'Age', 'Outcome']
pima1 = pima.copy()
pima1 = pima1.drop('Outcome', axis=1)
print(pima1)
x = pima1

target = pima['Outcome']
le = LabelEncoder()
target = le.fit_transform(target)
print(target)
y = target

# Split dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=40)
print("Training split input- ", X_train.shape)
print("Testing split input- ", X_test.shape)

# Create Decision Tree classifier model
clf = DecisionTreeClassifier()
# Train Decision Tree Classifier
clf.fit(X_train, Y_train)
print("Decision tree classifier created")

# Predict the response for test data
Y_pred = clf.predict(X_test)
print("Classification report - \n", classification_report(Y_test,Y_pred))
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))

# Create confusion metrix
cm = confusion_matrix(Y_test,Y_pred)
print(cm)
plt.figure(figsize=(8,8))
sns.heatmap(data=cm, linewidths=0.5, annot=True, square=True, cmap='Blues')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
all_sample_title = "Accuracy Score:{0}" .format(clf.score(X_test,Y_test))
plt.title(all_sample_title, size=15)
plt.savefig('figure1.png')


# Visualising decision tree
plt.figure(figsize=(50,50))
dec_tree = plot_tree(decision_tree=clf, feature_names=pima1.columns,
                     class_names=["1","0"], filled= True, precision=4, rounded= True)
plt.savefig('figure.png')