wine_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",header = None)
num_clusters = list(range(1,11))
inertias = []
for k in num_clusters:
  model = KMeans(n_clusters = k)
  model.fit(wine_data)
  inertias.append(model.inertia_)
  
plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')

plt.show()

#After getting a suitable K. Train and predict

model = KMeans(n_clusters = 4)
model.fit(wine_data)
labels = model.predict(wine_data)
print(labels)