#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <--------------------- Formateo de Tablas ---------------------------------->

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una unica fila de datos de la tabla.
        '''
        raise NotImplementedError()

# <---------------------- Formato txt ---------------------------------------->

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))
    
    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

# <------------------------ Formato csv -------------------------------------->

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

# <-------------------------- Formato HTML ----------------------------------->

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
    
    def fila(self, data_fila):
        print('<tr>', end='')
        for d in data_fila:
            print(f'<th>{d}</th>', end='')
        print('</tr>')

# <--------------------------- Formateador ----------------------------------->

def crear_formateador(fmt):
    ''''
    Creo formato de salida segun indique el usuario
    '''
    if fmt == 'txt':
        return FormatoTablaTXT() # Formato TXT
    elif fmt == 'csv':
        return FormatoTablaCSV() # Formato CSV
    elif fmt == 'html':
        return FormatoTablaHTML() # Formato HTML
    else:
        raise RuntimeError(f'Unknown format {fmt}')

# <--------------------------- Imprimir -------------------------------------->

def imprimir_tabla(data, columnas, formato):
    formato.encabezado(columnas)
    for row in data:
        formato.fila(getattr(row, columnas))
#%%
