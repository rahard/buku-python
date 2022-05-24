# contoh program untuk k-means
import pandas as pd
import matplotlib.pyplot as plt

# baca data dahulu
df = pd.read_csv('cluster.csv', header=None)
df.columns = ['x', 'y']
#print(df)
# tampilkan jika dibutuhkan
df.plot.scatter(x = 'x', y='y', c='red')
plt.show()

# mari kita lakukan k-means clustering
# silahkan diubah-ubah jumlah clusternya di variabel n_clusters
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

# tampilkan secara visual
plt.scatter(df['x'],df['y'], c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
plt.show()
