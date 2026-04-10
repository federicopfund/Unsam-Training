# -*- coding: utf-8 -*-
"""

@author: federico pfund
"""
#%%
import random
from matplotlib import pyplot as plt
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
    mediana = sorted(big_Data)[int(len(big_Data)/2)]
    print(f'| Minimo:{minimo:.2f} | Maximo:{maximo:.2f} | Promedio:{promedia:.2f} | Media:{mediana:.2f} |')
    return big_Data
    
tempera=termometro(99,37.5)# ingresan 2 parametros(temperatura, y temeperatura media)
#%%
