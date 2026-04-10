# -*- coding: utf-8 -*-
"""
@author: feder
"""
import random
import numpy as np
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album
figus_total = 670
def album_incompleto(album):
   
    estado = 0 in album
    return estado
def comprar_figu(figus_total):
    numero_figu = random.randint(0,figus_total-1)
    return numero_figu
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1
    cantidad_figu = album.sum()
    return cantidad_figu
cantidad_figu = cuantas_figus(figus_total)
