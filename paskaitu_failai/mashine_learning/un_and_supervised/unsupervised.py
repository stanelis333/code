import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import os
os.environ['LOKY_MAX_CPU_COUNT'] = '8'

data = pd.read_csv("C:\\code\\paskaitu_failai\\mashine_learning\\un_and_supervised\\databases\\Mall_Customers.csv")
# print(data)

X = data[['Annual Income (k$)', 'Spending Score (1-100)']].values
# print(X[:5])

inertia_values = []
k_values = range(1, 11) 

for k in k_values:
    kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, random_state=42)
    kmeans.fit(X)
    inertia_values.append(kmeans.inertia_)

plt.figure(figsize=(10, 7))
plt.plot(k_values, inertia_values, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()


kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=300, random_state=42)
y_kmeans = kmeans.fit_predict(X)

cluster_centers = kmeans.cluster_centers_

plt.figure(figsize=(10, 7))
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X')
plt.title('K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()


inertia = kmeans.inertia_
silhouette_avg = silhouette_score(X, y_kmeans)
davies_bouldin = davies_bouldin_score(X, y_kmeans)
calinski_harabasz = calinski_harabasz_score(X, y_kmeans)

print(f'Inertia: {inertia}')
print(f'Silhouette Score: {silhouette_avg}')
print(f'Davies-Bouldin Index: {davies_bouldin}')
print(f'Calinski-Harabasz Index: {calinski_harabasz}')

išvados = ("\n1.Optimalus klasterių skaičius: Remiantis Elbow metodu yra 5.\n"
           "2.Klasterių charakteristikos: Klientai yra suskirstyti pagal metines pajamas ir išlaidų rodiklį, rodant aiškius segmentus, tokius kaip aukštos pajamos-mažos išlaidos, mažos pajamos-didelės išlaidos ir pan.\n"
           "3.Klasterių kokybė: (Silhouette Score, Davies-Bouldin Index ir Calinski-Harabasz Index) rodo, kad klasterizacija yra pakankamai gera, o Silhouette Score nurodo, kaip gerai  yra atskirti klasteriai.")
print(f"\nIšvados: {išvados}")