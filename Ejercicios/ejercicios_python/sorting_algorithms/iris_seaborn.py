#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%

# <----------------------------s Importamos s-------------------------------->

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#%%
#<--------------------------------s Data_Frame s------------------------------>
# Creo Dataframe de flores
iris_dataset = load_iris()

iris_dataframe = pd.DataFrame(iris_dataset['data'],
                              columns = iris_dataset.feature_names) 
iris_dataframe['target'] = iris_dataset['target']

# Agrego los nombres a las claves [0,1,2] de iris_dataset['target']
# Para cada valor [0,1,2] asigno el nombre
# por ['setosa', 'versicolor', 'virginica'] de iris_dataset['target_names']

d_names = dict(zip([0,1,2], iris_dataset['target_names']))

names = [d_names[iris_dataset['target'][i]] \
         for i in range (len(iris_dataset['target']))]
 # Creo la columna en el dataframe
iris_dataframe['target_names'] = names 

# Eligo las variables para explorar.
x_vars=['sepal length (cm)', 'sepal width (cm)',
        'petal length (cm)', 'petal width (cm)']

y_vars=['sepal length (cm)', 'sepal width (cm)',
        'petal length (cm)', 'petal width (cm)']
#%%
# <---------------------------s Grafico s--------------------------------->
g = sns.pairplot(data = iris_dataframe, x_vars = x_vars, y_vars = y_vars,
                 hue = 'target_names', diag_kind='hist', markers=["o", "s", "D"],
                 height = 2)
            
#<----------------------- Título de gráfico ------------------------------>
g.fig.suptitle("Data Frame iris (Fisher) exploración de datos por tamaño\n"
             "sépalos vs. tétalos, largo y ancho")
plt.subplots_adjust(top= 0.9)

plt.show()
