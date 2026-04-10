# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:05:37 2021

@author: federico pfund

"""
#   Ejercicio de errores en el codigo

#%%
#Ejercio 3.1 Semántica
#ERROR: Si se considera que este algoritmo determina si el string tiene un caracter igual a,
#       de ser asi, podemos decir que no contempla los casos en la cual el string ingresa una
#       A en mayuscula, por lo que no reconoce ese caracter como a. 
#       
#       Para el ultimo llamado de la funcion tenemos el error de que retorna false un string
#       que SI tiene a, el motivo de tal errror es que si estrictamente el primer elemnto no es una 
#       a, el programa no seguira analizando los otros caracteres  que constituyen  al string. 
#       (ERROR de Semántica).
#CORRECCION: Para contruir una buena semantica que funcione con la logica del nombre en la que 
#           dicha funcion que representa. habra que incluir mayuscula o convertir el string analizado
#           a minuscula.
#           Por otro lado podemos mejorar el diseño para que analice todos los caracteres que constituyen
#           al string,la manera de hacerlo preguntado si EXPRECION[I] se encuenta en el string "aA" de ser true
#           lo retorna a la pantalla, de ser false sigue incrementando i para evaluar otros elementos del string.
# Arreglo:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
            i += 1
        
        else:
            i += 1
    return False
        
tiene_a('UNSAM 2a020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 4.1: Semántica defectuosa.
#
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
        
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.2 Sintaxis
#ERROR: Error de sintaxis ya que cada funcion que se quiera definir tendra :
#       cierren la funcion definida,por lo que genera un error de 
#       tipo: SyntaxError
#CORRECCION: Agregaremos los : punto para contemplar el SyntaxError,de la funcion, luego del while, y tambien
#           los del if, tambien cambiaremos de semantica en el condicional if, "=" por "in",de esta manera podemos incluir 
#           a las mayusculas A,y por ultimo retornaremos False y no Falso ya que no lo reconoce  como un  booleanos!! 

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aA':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.3 Tipos.
#ERROR: Esta funcion anda solamente para cadenas tipo string, en caso de ingresar un numero entero o flotante se rompe
#       y no se puede evaluar, el caso de la solucion es ingresar todo como tipo string, de no ser asi se tendra que levantar
#       esta condicion y evaluar los valores ingresado por el usuaria,para seleccionar de manera se tiene que evaluar el fragmento
#       analizado.
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno("1984")
#%%
#Ejercicio 3.4 Alcances.
#Error: Aqui el problema es que python para devolver un valor de una operacion,necesariamente se le pide que retorne dicho valor
#       esto reviza que tipo de operacion es necesaria para retornar el valor que se le pidio.. por lo que la manera era sacando 
#       el print y decirle a la funcion que retorne el valor de la operacion.. para que de un uso esto no puede ser printeado, ya 
#       que es una operacion matematica que tiene que devolver un entero o en su defecto un flotante, no puede ser un string..
#
#
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
suma(a,b)
#%%
#Ejercicio 3.5  Pisando memoria.
#Error: Es que en cada iteracion se le asignan nuevas valores a las claves que definne el diccionario
#       por lo que se actualiza en cada iteracion y lo que vemos la ultima como final..
#CORRECCION: Para dicha correccion mejoraremos la semantica de la funcion, primero declararemos 
#               filas con la estructura de dato que lea del archivo.. luego con la funcion zip harmamos los pares 
#               enlazando encavezados y filas.. 
#

from pprint import pprint
def leer_camion(nuevo_archivo):
    import csv
    camion = []
    
    try:
        with open(nuevo_archivo,"rt") as f:
            row =csv.reader(f)
            headers = next(row)        
            for line in row:
                try:#levantamos indexerror
                    fila = [line[0], int(line[1]), float(line[2])]
                    registro = dict(zip(headers,fila))
                    camion.append(registro)
                except IndexError:
                    pass
        return camion
        
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
data = leer_camion('../Data/camion.csv')
pprint(data)

#%%
