#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:32:25 2020

@author: rgrimson
"""
    
#%% funciones

def saludar(nombre):
    print('Hola,', nombre)

saludar('José')
saludar('Ana')

#%% funciones doble mas uno

def doble_mas_uno(n):
    r = 2*n
    r = r + 1
    return r


doble_mas_uno(5)
doble_mas_uno(12)
doble_mas_uno('a')


#%%

def suma(a,b):
    return a + b

#%% Módulos y funciones

import math

math.pi
math.sqrt(2)


#%% Usando una función en "inclusive.py"


frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
palabras_nuevas = []
for palabra in palabras:
    palabra_nueva = neutralizar_palabra(palabra)
    palabras_nuevas.append(palabra_nueva)
frase_t = ' '.join(palabras_nuevas)
print(frase_t)

#%%
def neutralizar_palabra(palabra):    
    punc = '''¡!()-[]{};:'"\, <>./¿?@#$%^&*_~'''
    palabra = palabra.strip(punc)
    if len(palabra)>=2:
        if palabra[-2]=='o':
            palabra_nueva=palabra[:-2]+'e'+palabra[-1]
        elif palabra[-1]=='o':
            palabra_nueva=palabra[:-1]+'e'
        else:
            palabra_nueva=palabra
    else:
       palabra_nueva=palabra
    return palabra_nueva

#%%
#strings
punc = '''¡!()-[]{};:'"\, <>./¿?@#$%^&*_~'''
palabra.strip()
palabra.strip(punc)


#%% Secuencias y cliclos
#Hay tres tipos de secuencias: cadenas, listas y tuplas.
#Se puede iterar sobre ellas:

s = [1, 4, 9, 16]
for i in s:
     print(i)
     
for c in "palabra":
    print(c)

for e in (1, 2, 4, 8, 16, 32):
    print(e)
    
#sobre tuplas hablamos en la clase escrita
#%%
bool("a")
bool([0])
bool(0.0001)

bool("False")


#%% for

cadena='Geringoso'
i = 0
for c in cadena:
    if c in 'aeiou':
        print(i,':', c)
    i += 1

#%% for + f-string

cadena='Geringoso'
i = 0
for c in cadena:
    if c in 'aeiou':
        print(f'{i:d}: {c:s}')
    i += 1        
        

#%% Diccionarios
estudiantes = {'Marília': 'Puerto Iguazú',
             'Verónica': 'Saavedra',
             'Claudio': 'San Martín',
             'Carolina': 'Gral. Villegas',
             'Gabriel': 'Villa Pueyrredón',
             'Franco': 'San Martín'
             }

#%%
print(estudiantes)
#%%
estudiantes['Elisa']='Alemania'
estudiantes['José']='Belgrano'
estudiantes['Alfredo']='Inglaterra'
estudiantes['Daniela']='Villa Pueyrredón'
#%%
print(estudiantes)
print(estudiantes['Verónica'])

estudiantes['Verónica']='Villa Urquiza'
print(estudiantes['Verónica'])

#%% f-Strings

for n in estudiantes:
    print(f'|{n:<8s} | {estudiantes[n]:^16s}|')



#%%
def linea_sep():
    print('-'*(8+16+5))

linea_sep()    
print(f'|{"nombre":<8s} | {"ciudad":^16s}|')
linea_sep()
for n in estudiantes:
    print(f'|{n:<8s} | {estudiantes[n]:^16s}|')
linea_sep()



#%% Archivos

f = open('Data/arboles.csv', 'rt')  
data = f.read()
print(data)

#%%
f.close()

#%%
nombre_archivo = 'Data/arboles.csv'
with open(nombre_archivo, 'rt') as archivo:
    for i, linea in enumerate(archivo):
        print(i, linea)

#%%
f = open('Data/arboles.csv', 'rt')
# o si hace falta aclararlo en tu SO
f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',')
encabezados
#%%
for line in f:
    fila = line.split(',')
    print(fila)

#%%
encabezados
fila


#%% zip

l=[]
f = open('Data/arboles.csv', 'rt')
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    #print(fila)
    registro = dict(zip(encabezados, fila))
    l.append(registro)



#%%



f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    for e,d in zip(encabezados,fila):
        el = e.strip("\n")
        dl = d.strip("\n")
        print(f'{el:>12s}: {dl}')
    print()



#%%

f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).strip("\n").split(',')
arboles = []
for line in f:
    fila = line.strip("\n").split(',')
    arbol = {}
    for e,d in zip(encabezados,fila):
        arbol[e]=d
    arboles.append(arbol)
    
