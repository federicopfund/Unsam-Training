#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%

#<----------------------------- Imports ------------------------------------>
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%

#<---------------------- ajuste_lineal_simple ----------------------------->
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%
#<------------------------- Variables ------------------------------------->
minx = 0
maxx = 200
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
#%%
#<------------------------- Ajuste lineal --------------------------------->
a, b = ajuste_lineal_simple(superficie, alquiler)
#%%
#<------------------------ Tendencia lineal ------------------------------->
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b
#%%
#<--------------------------- Plot ---------------------------------------->
g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#%%
#<--------------------- Error Cuadratico Medio ---------------------------->
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())

#%%   
# |====================Regrecion Lineal Multiple============================|

# <------------------- Tenemos en Cuenta la Antigüedad -------------------->
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0] 
#%%
data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie,
                            'antigüedad': antigüedad})
#%%
X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)
#%%
ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)
#%%
errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
#<-------------------- Error cuadratico medio ------------------------------>
print("ECM:", (errores**2).mean()) 
#%%