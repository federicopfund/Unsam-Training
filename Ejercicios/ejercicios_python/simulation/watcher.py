#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <---------------------- Funciones Generadores --------------------------------->
"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com """


# <------------------------------Imports------------------------------------->

#%%
import os
import time
import informe
#%%

# <---------------------------- Vigilar ------------------------------------->
def vigilar(filename):
  
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
# <-----------productor------------->
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.3)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        else:
            yield line

# <-------------imprecion solamente las que estan en el camion -------------->
if __name__ == '__main__':
    

    camion = informe.leer_camion ('../Data/camion.csv')
# <-------consumidor----------------->
    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
# <------- filtro ----------------->
        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
