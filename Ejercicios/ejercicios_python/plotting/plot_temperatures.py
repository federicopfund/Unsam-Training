# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import random

#%%
def termometro(N,media):
    big_Data=[]
    for i in range(N):
       temperatura= random.normalvariate(media,0.2)
       big_Data.append(temperatura)
    plt.plot(big_Data)
    plt.show()
    minimo = min(big_Data)
    maximo = max(big_Data)
    promedia = sum(big_Data)/N
    media = sorted(big_Data)[int(len(big_Data)/2)]
    print(f'| Minimo:{minimo:.2f} | Maximo:{maximo:.2f} | Promedio:{promedia:.2f} | Media:{media:.2f} |')
    return big_Data
    
tempera=termometro(999,37.5)# ingresan 2 parametros(temperatura, y temeperatura media)
#%%
a=np.array(tempera)
np.save('temperaturas.npy', a)
b=np.load('temperaturas.npy')
plt.hist(b,bins=50)
np.save('../Data/Temperaturas.npy', termometro)
#%%