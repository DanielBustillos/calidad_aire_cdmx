# coding=utf-8
# Definición de diccionarios y etiquetas para los contaminantes.
# Esto se define de manera manual para que cada grupo de O3, PM10 y PM2.5 tengan una paleta de colores consistente


def dic_etiquetas():
    dic_etiquetas= {'o3_max': 'O3',
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
    return dic_etiquetas


def dic_colores():
    dic_colores= {'o3_max': '#7f0000',
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
    return dic_colores

def colores_(ca):
    if ca == 'Buena':
        return '#99ca3a'
    if ca == 'Regular':
        return '#f7ec0f'
    if ca == 'Mala':
        return '#f8991d'
    if ca == 'Muy mala':
        return '#ed2124'
    if ca == 'Extremadamente mala':
        return '#7d287d'
    if ca == 'Peligrosa':
        return '#7e0023'

def color_leyenda_calidad_aire(vi):
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
