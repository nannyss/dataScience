from math import sqrt
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X,y = make_blobs(n_samples=500, centers=20, random_state=999)
plt.scatter(X[:,0], X[:,1])
plt.xlim(0,9)
plt.ylim(0,9)
plt.grid()
plt.show()


Kmeans = KMeans(n_clusters=3,init="K-means++",max_iter=300,n_init=10)
y_predict = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1])
plt.xlim(0,9)
plt.ylim(0,9)
plt.grid()
plt.show()


from math import sqrt
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
X, y = make_blobs(n_samples=500, centers=20, random_state=999)
plt.scatter(X[:,0], X[:,1])

def optimal_number_of_clusters(wcss):
    x1, y1 = 1, wcss[0]
    x2, y2 = 19, wcss[len(wcss)-1]
    distances = []
    for i in range(len(wcss)):
        x0 = i + 1
        y0 = wcss[i]
        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
    
    return distances.index(max(distances)) + 1

wcss = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
n = optimal_number_of_clusters(wcss)
print(n)
print (wcss)


kmeans = KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1],c=pred_y)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=70,c='red')

plt.grid()
plt.show()
print('soma os quadrados intra-clusters (wcss)',kmeans.inertia_)