# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:42:54 2019

@author: user
"""
#The data set consists of 50 samples from each of three species of Iris
#Iris setosa,
#Iris virginica and
#Iris versicolor.
#Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres.


import numpy as np
from sklearn import datasets


iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
#print(iris_data[0], iris_data[79], iris_data[100])
#print(iris_labels[0], iris_labels[79], iris_labels[100])

#impartim random datele intr-un set de 12 vectori de invatare si restul de testare
#np.random.seed(42)
indices = np.random.permutation(len(iris_data))
n_training_samples = 10
learnset_data = iris_data[indices[:-n_training_samples]]
learnset_labels = iris_labels[indices[:-n_training_samples]]
testset_data = iris_data[indices[-n_training_samples:]]
testset_labels = iris_labels[indices[-n_training_samples:]]
#print(learnset_data[:4], learnset_labels[:4])
#print(testset_data[:4], testset_labels[:4])

def distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)

#The function 'get_neighbors returns a list with 'k' neighbors, 
#which are closest to the instance 'test_instance':

def get_neighbors(training_set, 
                  labels, 
                  test_instance, 
                  k, 
                  distance=distance):
    """
    get_neighors calculates a list of the k nearest neighbors
    of an instance 'test_instance'.
    The list neighbors contains 3-tuples with  
    (index, dist, label)
    where 
    index    is the index from the training_set, 
    dist     is the distance between the test_instance and the 
             instance training_set[index]
    distance is a reference to a function used to calculate the 
             distances
    """
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors
"""testarea functiei:
for i in range(2):
    neighbors = get_neighbors(learnset_data, 
                              learnset_labels, 
                              testset_data[i], 
                              3, 
                              distance=distance)
    print(i, 
          testset_data[i], 
          testset_labels[i], 
          neighbors)"""
    
#fct vote returneaza cea mai des intalnita clasa 
#dintre vecinii lui test_instace        
from collections import Counter

def vote(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    return class_counter.most_common(1)[0][0]

"""testarea fctiei pe setul nostru de invatare"""
for i in range(n_training_samples):
    neighbors = get_neighbors(learnset_data, 
                              learnset_labels, 
                              testset_data[i], 
                              4, 
                              distance=distance)
    print("index: ", i, 
          ", result of vote: ", vote(neighbors), 
          ", label: ", testset_labels[i], 
          ", data: ", testset_data[i])
