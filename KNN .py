import pandas as pd
import numpy as np
import math
import operator

filepath = r'J:\ESDS\Training\SEM 2\staff notes\Python\Practicals_Python_ML\GroupB\KNN\iris.csv'

# Read data
data = pd.read_csv(filepath)
# Show top 5 records
print(data.head(5))


# Defining a function which calculates euclidean distance between two data points
def euclideanDistance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += np.square(data1[x] - data2[x])
    return np.sqrt(distance)


# Defining our KNN model
def knn(trainingSet, testInstance, k):
    distances = {}
    sort = {}
    length = testInstance.shape[1]
    
    # Calculating euclidean distance between each row of training data and test data
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
        
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []
    
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    classVotes = {}
    
    
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
   
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], neighbors)
  

testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)


# Setting number of neighbors = 1
print('\n\nWith 1 Nearest Neighbour \n\n')
k = 1

# Running KNN model
result,neigh = knn(data, test, k)

# Predicted class
print('\nPredicted Class of the datapoint = ', result)

# Nearest neighbor
print('\nNearest Neighbour of the datapoints = ',neigh)

print('\n\nWith 3 Nearest Neighbours\n\n')
# Setting number of neighbors = 3 
k = 3 
# Running KNN model 
result,neigh = knn(data, test, k) 

# Predicted class 
print('\nPredicted class of the datapoint = ',result)

# Nearest neighbor
print('\nNearest Neighbours of the datapoints = ',neigh)

print('\n\nWith 5 Nearest Neighbours\n\n')
# Setting number of neighbors = 3 
k = 5
# Running KNN model 
result,neigh = knn(data, test, k) 

# Predicted class 
print('\nPredicted class of the datapoint = ',result)

# Nearest neighbor
print('\nNearest Neighbours of the datapoints = ',neigh)

# verify with sklearn knn classifier
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data.iloc[:,0:4].values, data['variety'])

# Predicted class
print(neigh.predict(test))

# 3 nearest neighbors
print(neigh.kneighbors(test)[1])
# -> [[141 139 120]]
