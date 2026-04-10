#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:19:02 2021

@author: rgrimson
"""

a = 12
a += 1
#%%%

s="""Hola mundo
sigue abajo"""



#%% Celda de Geringoso
palabra = "guerra"
papalapabrapa = ''
for c in palabra:
    papalapabrapa += c
    if c in "aeiou":
        papalapabrapa += 'p' + c
    elif c in "AEIOU":
        papalapabrapa += 'P' + c

#%%       
#%%
def geringoso_lazy(palabra): # type: ignore
    for c in palabra:
        yield c
        if c in "aeiou":
            yield 'p' + c
        elif c in "AEIOU":
            yield 'P' + c
geru = geringoso_lazy("asdfrd")

geru_result = ''.join(geru)
print(geru_result)



#%%
def transformar_palabra_lazy(palabra):
    if palabra[-1] == 'o':
        yield palabra[:-1] + 'e'
    elif len(palabra) >= 2 and palabra[-2] == 'o':
        yield palabra[:-2] + 'e' + palabra[-1]
    else:
        yield palabra
#%%
# Ejemplo de uso
palabra = "lazy"
palabra_transformada = ''.join(transformar_palabra_lazy(palabra))
print(palabra_transformada)


#%%         #lazy evaluation
palabra= "y"

if palabra[-1] == 'o':
    palabre = palabra[:-1] + 'e'
elif len(palabra)>=2 and palabra[-2] == 'o':
    palabre = palabra[:-2] + 'e' + palabra[-1]

#%%
def geringoso_lazy(palabra):
    for c in palabra:
        yield c
        if c in "aeiou":
            yield 'p' + c
        elif c in "AEIOU":
            yield 'P' + c

# Ejemplo de uso
palabra = "guerra"
palabra_transformada = ''.join(geringoso_lazy(palabra))
print(palabra_transformada)



#%%


def neutralizar_palabra(palabra):    
    if len(palabra)>=2 and palabra[-2]=='o':
        palabra_nueva=palabra[:-2]+'e'+palabra[-1]
    elif palabra[-1]=='o':
        palabra_nueva=palabra[:-1]+'e'
    else:
        palabra_nueva=palabra
    return palabra_nueva

#%%


frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
palabras_nuevas = []
for palabra in palabras:
    palabra_nueva = neutralizar_palabra(palabra)
    palabras_nuevas.append(palabra_nueva)
frase_t = ' '.join(palabras_nuevas)
print(frase_t)
# %%
