# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:12:24 2019

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets


iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target

def distance(instance1, instance2):

    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)


def get_neighbors(training_set, 
                  labels, 
                  test_instance, 
                  k, 
                  distance=distance):
    
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors

from collections import Counter

def vote(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    return class_counter.most_common(1)[0][0]

k = np.zeros(50)
for j in range (50):
    indices = np.random.permutation(len(iris_data))
    n_training_samples  = j
    learnset_data = iris_data[indices[:-n_training_samples]]
    learnset_labels = iris_labels[indices[:-n_training_samples]]
    testset_data = iris_data[indices[-n_training_samples:]]
    testset_labels = iris_labels[indices[-n_training_samples:]]
    for i in range(n_training_samples):
        neighbors = get_neighbors(learnset_data, 
                              learnset_labels, 
                              testset_data[i], 
                              1, 
                              distance=distance)
        if vote(neighbors)!=testset_labels[i]:
           k[j]=k[j]+1
           
plt.plot(k, 'ro')
plt.axis([0, 50, 0, 5])
plt.show()