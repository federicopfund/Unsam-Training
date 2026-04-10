# fileparse.py

import csv
#%%
def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros con conversión de tipos.
    '''
    if select and not has_headers:
        raise RuntimeError('para seleccionar columnas, el archivo tiene que tener encabezado')

    rows = csv.reader(lines)

    # Leer los encabezados (si hubiera)
    headers = next(rows) if has_headers else []

    # Si se seleccionaron columnas, generar sus índices
    if select:
        indices = [ headers.index(col) for col in select ]
        headers = select

    registros = []
    for i, row in enumerate(rows, 1):
        if not row:     # Saltear filas vacías
            continue

        # Si se seleccionaron columnas, tomar de la fila esos datos
        if select:
            row = [ row[index] for index in indices]

        # Convertir los tipos de la fila
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {i}: No pude convertir {row}")
                    print(f"Fila {i}: Motivo {e}")
                continue

        # Hacer un diccionario o una tupla
        if headers:
            registro = dict(zip(headers, row))
        else:
            registro = tuple(row)
        registros.append(registro)

    return registros
