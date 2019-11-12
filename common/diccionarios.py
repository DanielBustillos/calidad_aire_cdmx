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
    color= ''
    leyenda= ''
    if 0 <= vi <= 50:
        color= '#99ca3a'
        leyenda= 'Buena'
    if 50 < vi <= 100:
        color = '#f7ec0f'
        leyenda = 'Regular'
    if 100 < vi <= 150:
        color = '#f8991d'
        leyenda = 'Mala'
    if 150 < vi <= 200:
        color = '#ed2124'
        leyenda = 'Muy mala'
    if 200 < vi <= 300:
        color = '#7d287d'
        leyenda = 'Extremadamente mala'
    if 300 < vi <= 500:
        color = '#7e0023'
        leyenda = 'Peligrosa'

    return color, leyenda

def dic_colores_gauge():
    dic_colores_gauge = {'gradient': True,
                         'ranges': {'#99ca3a': [0, 50],
                                    '#f7ec0f': [50, 100],
                                    '#f8991d': [100, 150],
                                    '#ed2124': [150, 200],
                                    '#7d287d': [200, 300],
                                    '#7e0230': [300, 350]}}
    return dic_colores_gauge