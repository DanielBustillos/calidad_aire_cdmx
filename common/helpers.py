# coding=utf-8

"""Funciones útiles y diccionarios llamados por los scripts principales (tablero.py y/o documentacion.py).
Pueden ser recicladas para otros usos.

Ejemplo:
    Llamar a la función (definida en este módulo)

    $ indice_PM10(fila, 'o3_predicted_ppm')

    Lo cual tomará todas las filas (fila) de la columna 'o3_predicted_ppm' y hará la conversión a micro gramos sobre
    metro cúbico.

"""

def convertir_ppm(fila, columna):
    """Conversión de unidad de medición del contaminante de partículas por billón (ppb) a partículas por millón (ppm).

    Parameters
    ----------
    fila: serie de pandas
          Una fila de un dataframe de pandas.
    columna: string (cadena de texto)
             El nombre de una columna del dataframe de pandas que contiene la concentración del contaminante de interés.

    Returns
    -------
    ppm: float
         La cantidad del contaminante elegido en unidades de partículas por millón (ppm)
    """
    ppm=fila[columna]/1000
    return ppm


def indice_PM10(fila, columna):
    """Cálculo del índice de calidad del aire para el PM10 (usando datos de micro gramo sobre metro cúbico).

    Las operaciones que se realizan aquí son una normalización para que cada contaminante se mida de acuerdo al índice
    de calidad del aire. Esta función se ocupa de calcular el índice usando la concentración dada del PM10.

    Parameters
    ----------
    fila: serie de pandas
          Una fila de un dataframe de pandas.
    columna: string (cadena de texto)
             El nombre de una columna del dataframe de pandas que contiene la concentración del contaminante de interés.

    Returns
    -------
    indice: float
            El índice de calidad del aire del PM10.
    """
    if fila[columna] >= 0 and fila[columna] <= 40:
        indice = round(1.2500 * (fila[columna]))
        return indice
    if fila[columna] >= 41 and fila[columna] <= 75:
        indice = round((1.4412 * (fila[columna] - 41)) + 51)
        return indice
    if fila[columna] >= 76 and fila[columna] <= 214:
        indice = round((0.3551 * (fila[columna] - 76)) + 101)
        return indice
    if fila[columna] >= 215 and fila[columna] <= 354:
        indice = round((0.3525 * (fila[columna] - 215)) + 151)
        return indice
    if fila[columna] >= 355 and fila[columna] <= 424:
        indice = round((1.4348 * (fila[columna] - 355)) + 201)
        return indice
    if fila[columna] >= 425 and fila[columna] <= 504:
        indice = round((1.2532 * (fila[columna] - 425) + 301))
        return indice
    if fila[columna] >= 505 and fila[columna] <= 604:
        indice = doun((1.0000 * (fila[columna] - 505) + 401))
        return indice
    
    
def indice_O3(fila, columna):
    """Cálculo del índice de calidad del aire para el O3 (usando datos convertidos a ppm).

    Las operaciones que se realizan aquí son una normalización para que cada contaminante se mida de acuerdo al índice
    de calidad del aire. Esta función se ocupa de calcular el índice usando la concentración dada del O3.

    Parameters
    ----------
    fila: serie de pandas
          Una fila de un dataframe de pandas.
    columna: string (cadena de texto)
             El nombre de una columna del dataframe de pandas que contiene la concentración del contaminante de interés.

    Returns
    -------
    indice: float
            El índice de calidad del aire del O3.
    """
    if fila[columna] >= 0.000 and fila[columna] <= 0.070:
        indice = round(714.29 * (fila[columna]))
        return indice
    if fila[columna] >= 0.071 and fila[columna] <= 0.095:
        indice = round((2041.67 * (fila[columna] - 0.071)) + 51)
        return indice
    if fila[columna] >= 0.096 and fila[columna] <= 0.154:
        indice = round((844.83 * (fila[columna] - 0.096)) + 101)
        return indice
    if fila[columna] >= 0.155 and fila[columna] <= 0.204:
        indice = round((1000.00 * (fila[columna] - 0.155)) + 151)
        return indice
    if fila[columna] >= 0.205 and fila[columna] <= 0.404:
        indice = round((497.49 * (fila[columna] - 0.205)) + 201)
        return indice
    if fila[columna] >= 0.405 and fila[columna] <= 0.504:
        indice = round((1000.00 * (fila[columna] - 0.405) + 301))
        return indice
    if fila[columna] >= 0.505 and fila[columna] <= 0.604:
        indice = round((1000.00 * (fila[columna] - 0.505) + 401))
        return indice