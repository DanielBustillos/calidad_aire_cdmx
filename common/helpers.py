import pandas as pd
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
    if 0 <= fila[columna] <= 40:
        indice = round(1.2500 * (fila[columna]))
        return indice
    if 41 <= fila[columna] <= 75:
        indice = round((1.4412 * (fila[columna] - 41)) + 51)
        return indice
    if 76 <= fila[columna] <= 214:
        indice = round((0.3551 * (fila[columna] - 76)) + 101)
        return indice
    if 215 <= fila[columna] <= 354:
        indice = round((0.3525 * (fila[columna] - 215)) + 151)
        return indice
    if 355 <= fila[columna] <= 424:
        indice = round((1.4348 * (fila[columna] - 355)) + 201)
        return indice
    if 425 <= fila[columna] <= 504:
        indice = round((1.2532 * (fila[columna] - 425) + 301))
        return indice
    if 505 <= fila[columna] <= 604:
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
    if 0.000 <= fila[columna] <= 0.070:
        indice = round(714.29 * (fila[columna]))
        return indice
    if 0.071 <= fila[columna] <= 0.095:
        indice = round((2041.67 * (fila[columna] - 0.071)) + 51)
        return indice
    if 0.096 <= fila[columna] <= 0.154:
        indice = round((844.83 * (fila[columna] - 0.096)) + 101)
        return indice
    if 0.155 <= fila[columna] <= 0.204:
        indice = round((1000.00 * (fila[columna] - 0.155)) + 151)
        return indice
    if 0.205 <= fila[columna] <= 0.404:
        indice = round((497.49 * (fila[columna] - 0.205)) + 201)
        return indice
    if 0.405 <= fila[columna] <= 0.504:
        indice = round((1000.00 * (fila[columna] - 0.405) + 301))
        return indice
    if 0.505 <= fila[columna] <= 0.604:
        indice = round((1000.00 * (fila[columna] - 0.505) + 401))
        return indice


def no_operar_nan(valor_1, valor_2):
    """Comparar dos valores, saber si al menos uno es nulo.

    Se encuentra primero si alguno de los dos valores son nulos, si este es el caso se regresa un NaN. De lo contrario
    se comparan ambos valores y se halla el máximo. Dependiendo del valor que sea el mayor se etiqueta a que contaminante
    pertenece, si a PM10 u O3.

    Parameters
    ----------
    valor_1: float
             Índice de calidad del aire de un contaminante (O3).

    valor_2: float
             Índice de calidad del aire de un contaminante (PM10).

    Returns
    -------
    resultado: float o NaN
               El índice de calidad del aire mayor entre O3 y PM10.

    etiqueta: string ('O3' o 'PM10')
    """
    resultado=0
    if pd.isnull(valor_1) or pd.isnull(valor_2):
        resultado=float('NaN')
        return resultado
    else:
        resultado=int(round(max(valor_1, valor_2)))
        if valor_1 > valor_2:
            return 'O3', resultado
        else:
            return 'PM10', resultado


def color_leyenda_calidad_aire(vi):
    """Asignación de colores y etiqueta de acuerdo al valor del índice de calidad del aire.
    """
    color = ''
    color_opaco = ''
    leyenda = ''
    if 0 <= vi <= 50:
        color = '#99ca3a'
        color_opaco = '#cce29a'
        leyenda = 'Buena'
    if 50 < vi <= 100:
        color = '#f7ec0f'
        color_opaco = '#fbf4a3'
        leyenda = 'Regular'
    if 100 < vi <= 150:
        color = '#f8991d'
        color_opaco = '#ffc98b'
        leyenda = 'Mala'
    if 150 < vi <= 200:
        color = '#ed2124'
        color_opaco = '#f59678'
        leyenda = 'Muy mala'
    if 200 < vi <= 300:
        color = '#7d287d'
        color_opaco = '#b087b1'
        leyenda = 'Extremadamente mala'
    if 300 < vi <= 500:
        color = '#7e0023'
        color_opaco = '#c77f93'
        leyenda = 'Peligrosa'

    return color, color_opaco, leyenda


def rectangulos(maximo, fecha_actual, inicio_rango, fecha_max):
    """Construcción de los rectángulos de color que sirven para determinar visualmente en que nivel de "peligrosidad"
    se encuentra el índice de calidad del aire de acuerdo a la fecha. Estos rectángulos se agregan a la gráfica de
    líneas que aparece en el tablero del pronóstico de calidad del aire.
    """
    shapes = []
    verde_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 0, 'x1': fecha_actual,
                      'y1': 50, 'fillcolor': '#99ca3a', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    verde = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 0, 'x1': fecha_max, 'y1': 50,
             'fillcolor': '#99ca3a', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    amarillo_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 51, 'x1': fecha_actual,
                     'y1': 100, 'fillcolor': '#f9eb10', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    amarillo = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 51, 'x1': fecha_max, 'y1': 100,
               'fillcolor': '#f9eb10', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    naranja_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 101, 'x1': fecha_actual,
                     'y1': 150, 'fillcolor': '#fa981d', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    naranja = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 101, 'x1': fecha_max, 'y1': 150,
               'fillcolor': '#fa981d', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    rojo_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 151, 'x1': fecha_actual,
                  'y1': 200, 'fillcolor': '#ee2225', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    rojo = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 151, 'x1': fecha_max, 'y1': 200,
            'fillcolor': '#ee2225', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    morado_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 201, 'x1': fecha_actual,
                    'y1': 300, 'fillcolor': '#7d287d', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    morado = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 201, 'x1': fecha_max, 'y1': 300,
                    'fillcolor': '#7d287d', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    vino_opaco = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': inicio_rango, 'y0': 301, 'x1': fecha_actual,
                  'y1': 500, 'fillcolor': '#7e0023', 'opacity': 0.3, 'layer': 'below', 'line_width': 0}
    vino = {'type': 'rect', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 301, 'x1': fecha_max, 'y1': 500,
                    'fillcolor': '#7e0023', 'opacity': 0.6, 'layer': 'below', 'line_width': 0}
    if maximo <= 150:
        final_rango = 150
        linea = {'type': 'line', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 0, 'x1': fecha_actual,
                 'y1': final_rango, 'line': {'color': 'MediumPurple', 'width': 1, 'dash': 'dot'}}
        shapes = [linea, verde_opaco, verde, amarillo_opaco, amarillo, naranja_opaco, naranja]
    if 150 < maximo <= 200:
        final_rango = 200
        linea = {'type': 'line', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 0, 'x1': fecha_actual,
                 'y1': final_rango, 'line': {'color': 'MediumPurple', 'width': 1, 'dash': 'dot'}}
        shapes = [linea, verde_opaco, verde, amarillo_opaco, amarillo, naranja_opaco, naranja, rojo, rojo_opaco]
    if 200 < maximo <= 300:
        final_rango = 300
        linea = {'type': 'line', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 0, 'x1': fecha_actual,
                 'y1': final_rango, 'line': {'color': 'MediumPurple', 'width': 1, 'dash': 'dot'}}
        shapes = [linea, verde_opaco, verde, amarillo_opaco, amarillo, naranja_opaco, naranja, rojo_opaco, rojo,
                  morado_opaco, morado]
    if 300 < maximo <= 500:
        final_rango = 500
        linea = {'type': 'line', 'xref': 'x', 'yref': 'y', 'x0': fecha_actual, 'y0': 0, 'x1': fecha_actual,
                 'y1': final_rango, 'line': {'color': 'MediumPurple', 'width': 1, 'dash': 'dot'}}
        shapes = [linea, verde_opaco, verde, amarillo_opaco, amarillo, naranja_opaco, naranja, rojo_opaco, rojo,
                  morado_opaco, morado, vino_opaco, vino]
    return shapes

def dic_etiquetas():
    """Asignación de etiquetas correctas a las columnas originales del dataframe.

    Se guardan las etiquetas en forma de diccionario."""
    diccionario_etiquetas= {'o3_max': 'O3',
                    'o3_predicted_historico': 'O3 pronóstico histórico',
                    'o3_predicted': 'O3 pronóstico',
                    'tmp_mean_x': 'Temperatura promedio',
                    'pm10mean_max': 'PM10',
                    'pm10mean_max_ppb': 'PM10',
                    'pm10mean_predicted_historico': 'PM10 pronóstico histórico',
                    'pm10mean_predicted': 'PM10 pronóstico',
                    'rh_max': 'Humedad relativa',
                    'indice_PM10': 'PM10',
                    'indice_pronostico_PM10': 'PM10 pronóstico',
                    'indice_pronostico_hist_PM10': 'PM10 pronóstico histórico',
                    'indice_O3': 'O3',
                    'indice_pronostico_O3': 'O3 pronóstico',
                    'indice_pronostico_hist_O3': 'O3 pronóstico histórico'}
    return diccionario_etiquetas


def dic_colores():
    """Asignación de etiquetas de color a las columnas originales del dataframe.

    Los colores asignados se usarán para las visualizaciones en el tablero. Se guardan las etiquetas en forma de
    diccionario."""
    diccionario_colores= {'o3_max': '#7f0000',
                   'o3_predicted_historico': '#fb6a4a',
                    'o3_predicted': '#b30000',
                    'tmp_mean_x': '#35978f',
                    'pm10mean_max': '#023858',
                    'pm10mean_max_ppb': '#023858',
                    'pm10mean_predicted_historico': '#3690c0',
                    'pm10mean_predicted': '#0570b0',
                    'rh_max': '#c51b7d',
                    'indice_PM10': '#023858',
                    'indice_pronostico_PM10': '#0570b0',
                    'indice_pronostico_hist_PM10': '#74b5d8',
                    'indice_O3': '#7f0000',
                    'indice_pronostico_O3': '#b30000',
                    'indice_pronostico_hist_O3': '#fc9882'}
    return diccionario_colores
