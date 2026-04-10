# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
# propaga hacia un solo lado.
def propagar(lista):
    for i, t in enumerate(lista,start=0):
        if i-1>=0:
            if t==0  and lista[i-1]==1:
                lista[i] = 1
        if i + 1 < len(lista):
            if t==0 and lista[i+1]==1:
                lista[i]=1
    return lista
propagars= propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagars= propagar([ 0, 0, 0, 1, 0, 0])
#%%
#propaga hacia los 2 lados.
def propagar(lista):
    for i, t in enumerate(lista,start=0):
        if i-1>=0:
            if t==0  and lista[i-1]==1:
                lista[i] = 1
        for i in range(len(lista)-1,-1,-1):
            if i+1 < len(lista):
                if lista[i]==0 and lista[i+1]==1:
                    lista[i]=1
    return lista
propagars= propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagars= propagar([ 0, 0, 0, 1, 0, 0])
