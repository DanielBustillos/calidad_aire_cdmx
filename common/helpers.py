# coding=utf-8

"""Funciones útiles y diccionarios llamados por los scripts principales (tablero.py y/o documentacion.py).
Pueden ser recicladas para otros usos.

Ejemplo:
    Llamar a la función (definida en este módulo)

    $ indice_PM10(row, 'o3_predicted_ppm')

    Lo cual tomará todas las filas (row) de la columna 'o3_predicted_ppm' y hará la conversión a micro gramos sobre
    metro cúbico.

"""

def convertir_ppm(row, columna): #conversión de ppb a ppm
    """Conversión de unidad del contaminante de partículas por billón (ppb) a partículas por millón (ppm).

    Parameters
    ----------
    row: """
    ppm=row[columna]/1000
    return ppm