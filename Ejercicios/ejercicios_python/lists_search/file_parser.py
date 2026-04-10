# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:51:04 2021

@author: feder
"""

# fileparse.py
import csv
#%%
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros con conversión de tipos.
    '''
    rows = csv.reader(lines)
    data = []

    # Leer los encabezados (si los hay)
    headers = next(rows) if has_headers else []

    for row in rows:
        if not row:
            continue  # Skip empty rows

        # Filtrar solo las columnas seleccionadas
        if select:
            row = [row[headers.index(col)] for col in select]

        # Convertir tipos si se especifica
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Error en la conversión de tipos: {e}")
                continue

        data.append(row)

    return data

# Ejemplo de uso:
# with open('tu_archivo.csv', 'r') as file:
#     result = parse_csv(file, select=['Columna1', 'Columna2'], types=[int, float])
