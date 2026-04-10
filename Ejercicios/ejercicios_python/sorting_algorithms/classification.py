#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%

from sklearn.datasets import load_iris
iris_dataset = load_iris()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(X_train, y_train)

import numpy as np

x_new = np.array([[5, 2.9, 1, 0.2]])


import matplotlib.pyplot as plt
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(x_new[:, 1], x_new[:, 3], c = 'red')


prediction = knn.predict(x_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])


y_pred = knn.predict(X_test)

print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))


print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))

from sklearn.tree import DecisionTreeClassifier

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state = 0)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

prediction = knn.predict(x_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])


y_pred = clf.predict(X_test)

print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))


print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))