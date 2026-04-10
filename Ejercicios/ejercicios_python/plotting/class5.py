#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:32:25 2020

@author: rgrimson
"""
    
#Generación de número aleatorios
#%%

import random

dado = random.randint(1,6) # devuelve un entero aleatorio entre 1 y 6

print(random.randint(1,6))
#Si queremos simular una primera tirada del juego la generala tendremos que generar cinco valores al azar:
#%%
import random

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)
#%%


caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
tiro = random.choice(caras)
print(tiro)


#%%
caras = [1, 2, 3, 4, 5, 6]
print(random.choices(caras,k=5))

#%%
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    return max(tirada)==min(tirada)

#%%

N = 1000000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos aproximar la probabilidad de sacar generala servida mediante {prob:.6f}.')


#%%
N=1000000
prob=sum([es_generala(tirar()) for i in range(N)])/N


#%% suma de 5 dados
N = 10000000#00000
sumas=[sum(tirar()) for i in range(N)]
#%
import matplotlib.pyplot as plt


plt.hist(sumas,bins=26,density=True)

#%% sin reposicion
from pprint import pprint

palos = ['oro', 'copa', 'espada', 'basto']
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

naipes = [(valor,palo) for valor in valores for palo in palos]
pprint(naipes)
#%%
random.sample(naipes,k=3)
#%%
random.shuffle(naipes)


#%%
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N=100000
M=0
for i in range(N):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        M+=1
print(f'pi ~  {4*M/N:.5f}')


#%%

import matplotlib.pyplot as plt

N=1000
M=0
Xi = []
Yi = []
Xo = []
Yo = []

for i in range(N):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        Xi.append(x)
        Yi.append(y)
        M+=1
    else:
        Xo.append(x)
        Yo.append(y)

print(f'pi ~  {4*M/N:.5f}')

#%%
plt.clf()
plt.scatter(Xi,Yi,s=1)
plt.scatter(Xo,Yo,s=1)

#parámetros s, c y alpha

#%%
#REPASO:
import random


#random.randint()    Returns a random number between the given range

#random.shuffle()    Takes a sequence and returns the sequence in a random order

#random.choice()     un elemento
#random.choices()    k con repeticion

#random.sample()     k sin repeticion
#random.random()     Returns a random float number between 0 and 1
#random.gauss(mu, sigma)
#seed()              Initialize the random number generator

#%%

#el módulo numpy
import numpy as np

#vectores y matrices
v = np.array([1, 4, 9, 16])

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(m)
print(m.T)

m.dot(v)

m.shape
m.ndim
v.shape
v.ndim


#%%%

np.ones([3,3])
np.zeros([3,3])
np.eye(3)

#especificar el tipo de datos
np.eye(3,dtype=np.int64)


#%% partir un intervalo

np.linspace(0, 10, num = 11)
np.linspace(0, 10, num = 3)

np.arange(0, 11, 1)

np.arange(1, 11, step = 3)

np.linspace(0, 10)
np.linspace(0, 10).shape

#%%
#sort

v = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(v)
v.sort()
print(v)


#%%

#concatenar así o asá
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
#%%
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

x.shape
y.shape
np.concatenate((x, y), axis=0)

#%% cambiando la forma de un array
a = np.arange(6)
print(a)
a.reshape([2,3])

#%% seleccionar por condiciones

[1,2,3]<5

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

a > 5

W = (a > 5)
a[W]

~W
~W|W
~W&W


#%%

a

a[0]

a[0,:]

a[:,0]

b = a[0]
b
b[0]
b[0]=100
b[0]
b
a
#%%
# usar copy()
b = a[0].copy()
b[0] = 0
b
a
#%%

a
a.sum()
a.sum(axis=0)
a.sum(axis=1)


a.mean(axis=1)
a.max(axis=1)
a.min(axis=1)

#%%

u = a.mean(axis=1)
v = a.max(axis=1)
w = a.min(axis=1)

print(u,v,w)


u+v
w/v
w
w**2

5*w


#%%


# formulas en numpy
# ERROR CUADRATICO MEDIO (MSE)

#si predigo valores  (pesos de unas muestras, por ejemplo)
p = np.array([1.1,2.2,3.3,4.4,5.5])

#y la realidad era
r = np.array([1.0,2.4,3.2,4.8,5.1])

#los errores son
p-r

#%errores cuadráticos
((p-r)**2).mean()

#o, escrito de otra forma
1/5*np.sum(np.square(p-r))

#%%
#guardar datos en disco
#en forma compacta (binario)
np.save('matriz_A.npy', a)
np.load('matriz_A.npy')


# o en formato de texto
np.savetxt('matriz_A.csv', a)
np.loadtxt('matriz_A.csv')

