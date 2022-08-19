import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

filepath = r'J:\ESDS\Training\SEM 2\staff notes\Python\Practicals_Python_ML\GroupB\Clustering\Wholesale customers data.csv'

# Read dataset
data=pd.read_csv(filepath)
# Show top 5 results
print(data.head())

# Scaling of dataset
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# statistics of scaled data
print(pd.DataFrame(data_scaled).describe())

# Defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# Fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

# Fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# Converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)

# Value count of points in each clusters
frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()

# find centroids
centroids = kmeans.cluster_centers_
print(centroids)

# Plotting centres of clusters
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    #centroids,
    s=250, marker='*', c='red', edgecolor='black', label='centroids')

plt.legend(scatterpoints=1)
plt.grid()
plt.show()