#Mapper
from sklearn import datasets
import numpy as np
import operator
iris = datasets.load_iris()
X = iris.data[:, :4]  # we only take the first two features.
y = iris.target
# def knn_mapper(train_set, test_set):
train_set = X
test_set = X[124]
def euclidian_distance(x1, x2):
    dist = 0.0
    for i in range(0, len(x1)):
        dist+=np.sqrt(np.square((x2[i]-x1[i])))
        
    return dist
neighbour_dist = dict()
for x in range(len(train_set)):
    dist = euclidian_distance(train_set[x], test_set)
    
    neighbour_dist[x] = dist
    
sorted_neighbour = sorted(neighbour_dist.items(), key=operator.itemgetter(1))
class_neighbour = list()
for sn in sorted_neighbour:
    class_neighbour.append(y[sn[0]])
    
    print(y[sn[0]], '\t', 1)