#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <------------------------- Imports ---------------------------------------->
import informe
from formato_tabla import crear_formateador, imprimir_tabla
#%%
#
camion = informe.leer_camion('../Data/camion.csv')
formateador = crear_formateador('txt')
columnas = ['nombre', 'cajones']

imprimir_tabla(camion, columnas, formateador)