# App de índices de contaminantes (PM10 y O3)
import geopandas as gpd
import re
import dash_core_components as dcc
import dash_html_components as html
import json
import plotly.graph_objects as go
import locale

from datetime import timedelta

# Funciones y datos necesarios
from common.conversion_indice import indice_O3, indice_PM10, convertir_ppm, no_operar_nan
from common.diccionarios import dic_etiquetas, dic_colores, dic_colores_gauge, color_leyenda_calidad_aire
from data.db_conexion import df

# -----------------------------------------ESTRUCTURACIÓN DEL DATAFRAME------------------------------------------------#

# Establecemos el formato de hora local en español (México)
locale.setlocale(locale.LC_TIME, 'es_MX.utf8')

# Se definen las funciones de diccionarios como variables
dic_etiquetas = dic_etiquetas()
dic_colores = dic_colores()
dic_colores_gauge = dic_colores_gauge()

# Se establece el rango de fechas (7 días antes de la predicción) y se estructura el dataframe
fecha_max = max(df['fecha'])
fecha_min = min(df['fecha'])
inicio_rango = fecha_max - timedelta(days=5)
fecha_actual = fecha_max - timedelta(days=1)
posicion_x_etiqueta = fecha_actual + timedelta(hours=4)

mask = (df['fecha'] >= inicio_rango) & (df['fecha'] <= fecha_max)
df = df.loc[mask]

# Se reinicia el índice
rango = len(df.index)
df['indice'] = list(range(rango))
df.set_index('indice', inplace=True)

# Convertir O3 a ppm (para usar factores de conversión de la norma oficial)
df['o3_max_ppm'] = df.apply(lambda row: convertir_ppm(row, 'o3_max'), axis=1)
df['o3_predicted_ppm'] = df.apply(lambda row: convertir_ppm(row, 'o3_predicted'), axis=1)
df['o3_predicted_historico_ppm'] = df.apply(lambda row: convertir_ppm(row, 'o3_predicted_historico'), axis=1)

# Se usan las funciones definidas en conversion_indice.py para calcular el índice por contaminante
df['indice_PM10'] = df.apply(lambda row: indice_PM10(row, 'pm10mean_max'), axis=1)
df['indice_O3'] = df.apply(lambda row: indice_O3(row, 'o3_max_ppm'), axis=1)
df['indice_pronostico_PM10'] = df.apply(lambda row: indice_PM10(row, 'pm10mean_predicted'), axis=1)
df['indice_pronostico_O3'] = df.apply(lambda row: indice_O3(row, 'o3_predicted_ppm'), axis=1)
df['indice_pronostico_hist_PM10'] = df.apply(lambda row: indice_PM10(row, 'pm10mean_predicted_historico'), axis=1)
df['indice_pronostico_hist_O3'] = df.apply(lambda row: indice_O3(row, 'o3_predicted_historico_ppm'), axis=1)

# Se estructura el dataframe
df = df[['fecha', 'indice_PM10', 'indice_pronostico_PM10', 'indice_pronostico_hist_PM10',
         'indice_O3', 'indice_pronostico_O3', 'indice_pronostico_hist_O3']]

# Fechas formateadas a string
str_fecha_pronostico = fecha_max.strftime('%A %d de %B de %Y')
str_hora_pronostico = fecha_max.strftime('%H:%M hrs')

# Valores de índice actual (fecha_actual) y de pronóstico (fecha_max)
o3_actual = df.loc[df['fecha'] == fecha_actual, 'indice_O3'].iloc[0]
pm10_actual = df.loc[df['fecha'] == fecha_actual, 'indice_PM10'].iloc[0]
o3_pronostico = df.loc[df['fecha'] == fecha_max, 'indice_pronostico_O3'].iloc[0]
pm10_pronostico = df.loc[df['fecha'] == fecha_max, 'indice_pronostico_PM10'].iloc[0]
valor_indice = no_operar_nan(o3_actual, pm10_actual)
valor_indice_pronostico = no_operar_nan(o3_pronostico, pm10_pronostico)

# # Valores del índice de calidad del aire actual en texto y en rango de colores
# calidad_aire_actual= calidad_aire(valor_indice)
# c_texto_actual= c_texto(calidad_aire_actual)
#
# # Valores del índice de calidad del aire (pronóstico) en texto y en rango de colores
# calidad_aire_pronostico= calidad_aire(valor_indice_pronostico)
# c_texto_pronostico= c_texto(calidad_aire_pronostico)

# Rangos de indice de contaminación
marcas_indicador = [0, 50, 100, 150, 200, 300, 500]

# Colores y etiquetas de acuerdo al valor del índice de calidad del aire
color_actual, leyenda_actual = color_leyenda_calidad_aire(valor_indice)
color_pronostico, leyenda_pronostico = color_leyenda_calidad_aire(valor_indice_pronostico)

# -----------------------------------------MAPA DE CONTAMINACIÓN POR AGEB---------------------------------------------#
# Esto se realizó con datos viejos, para poder mostrar un demo en el tablero

with open('data/o3_ageb.json') as geofile:
    jfile = json.load(geofile)

geodf = gpd.read_file('data/O3_ageb.shp')


# Revisar la estructura del geojson y corregirla de ser necesario
def check_geojson(j_file):
    if 'id' not in j_file['features'][0].keys():
        if 'properties' in j_file['features'][0].keys():
            if 'id' in j_file['features'][0]['properties'] and j_file['features'][0]['properties']['id'] is not None:
                for k, feat in enumerate(j_file['features']):
                    j_file['features'][k]['id'] = feat['properties']['id']
            else:
                for k in range(len(j_file['features'])):
                    j_file['features'][k]['id'] = k
    return j_file


# Revisar el geofile
jdata = check_geojson(jfile)

# Establecer las variables de contaminación
z = geodf.O3_anual_f

# Graficar mapa

colorscale_mapa = [[0.0, '#99ca3a'],
                   [0.2, '#f7ec0f'],
                   [0.4, '#f8991d'],
                   [0.6, '#ed2124'],
                   [0.8, '#7d287d'],
                   [1.0, '#7e0230']]

data_mapa = go.Choroplethmapbox(z=z,
                                locations=geodf.id,
                                colorscale=colorscale_mapa,
                                colorbar={'thicknessmode': 'pixels',
                                          'thickness': 7,
                                          'outlinecolor': 'white',
                                          'title': {'text': 'indice',
                                                    'side': 'bottom'}},
                                geojson=jdata,
                                hoverinfo='all',
                                marker_line_width=0.1,
                                marker_opacity=0.5)

layout_mapa = go.Layout(title_x=0.5,
                        width=700,
                        height=700,
                        mapbox={'center': {'lat': 19.546232,
                                           'lon': -99.035067},
                                'style': 'carto-positron',
                                'zoom': 9.2},
                        margin={'l': 0,
                                'r': 0,
                                't': 0,
                                'b': 0})

figure_mapa = go.Figure(data=data_mapa,
                        layout=layout_mapa)


# ------------------------------------------------GRAFICAR LINE CHART---------------------------------------------------#
# Función que crea cada trazo, es decir una línea por contaminante y define si es sólida o punteada
def crear_trazo(df, y, name, color, x='fecha', width=3):
    regex = re.findall('pronóstico', name)
    if regex:
        trazo = go.Scatter(x=df[x],
                           y=df[y],
                           name=name,
                           line=dict(color=color, width=width, dash='dot'),
                           connectgaps=False)
    else:
        trazo = go.Scatter(x=df[x],
                           y=df[y],
                           name=name,
                           line=dict(color=color, width=width),
                           connectgaps=False)
    return trazo


data_lineas_a = [crear_trazo(df, col, dic_etiquetas[col], dic_colores[col]) for col in df.columns[1:]]
etiqueta_valor_actual = [go.Scatter(x=[posicion_x_etiqueta],
                                    y=[180],
                                    text=['valor actual'],
                                    mode='text',
                                    showlegend=False)]

data_lineas = data_lineas_a + etiqueta_valor_actual

layout_lineas = go.Layout(title={'text': 'Histórico y pronóstico de índice de calidad del aire'},
                          xaxis={'title': 'fecha',
                                 'tickangle': -45,
                                 'automargin': True,
                                 'tickformat': '%d %B / %H hrs',
                                 'showgrid': False,
                                 'nticks': 22},
                          yaxis={'title': 'índice de calidad del aire',
                                 'autorange': True,
                                 'showgrid': False,
                                 'showticklabels': True,
                                 'showline': False,
                                 'fixedrange': False},
                          shapes=[{'type': 'line',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': fecha_actual,
                                   'y0': 0,
                                   'x1': fecha_actual,
                                   'y1': 200,
                                   'line': {'color': 'MediumPurple',
                                            'width': 1,
                                            'dash': 'dot'}},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': inicio_rango,
                                   'y0': 0,
                                   'x1': fecha_actual,
                                   'y1': 50,
                                   'fillcolor': '#99ca3a',
                                   'opacity': 0.3,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': fecha_actual,
                                   'y0': 0,
                                   'x1': fecha_max,
                                   'y1': 50,
                                   'fillcolor': '#99ca3a',
                                   'opacity': 0.6,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': inicio_rango,
                                   'y0': 51,
                                   'x1': fecha_actual,
                                   'y1': 100,
                                   'fillcolor': '#f9eb10',
                                   'opacity': 0.3,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': fecha_actual,
                                   'y0': 51,
                                   'x1': fecha_max,
                                   'y1': 100,
                                   'fillcolor': '#f9eb10',
                                   'opacity': 0.6,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': inicio_rango,
                                   'y0': 101,
                                   'x1': fecha_actual,
                                   'y1': 150,
                                   'fillcolor': '#fa981d',
                                   'opacity': 0.3,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': fecha_actual,
                                   'y0': 101,
                                   'x1': fecha_max,
                                   'y1': 150,
                                   'fillcolor': '#fa981d',
                                   'opacity': 0.6,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': inicio_rango,
                                   'y0': 151,
                                   'x1': fecha_actual,
                                   'y1': 200,
                                   'fillcolor': '#ee2225',
                                   'opacity': 0.3,
                                   'layer': 'below',
                                   'line_width': 0},
                                  {'type': 'rect',
                                   'xref': 'x',
                                   'yref': 'y',
                                   'x0': fecha_actual,
                                   'y0': 151,
                                   'x1': fecha_max,
                                   'y1': 200,
                                   'fillcolor': '#ee2225',
                                   'opacity': 0.6,
                                   'layer': 'below',
                                   'line_width': 0}
                                  ]
                          )

figure_lineas = {'data': data_lineas,
                 'layout': layout_lineas}

# -----------------------------------------GRAFICAR INDICADORES--------------------------------------------------------#
#
# # Indicador actual
# data_1 = [{'title': {'text': leyenda_actual,
#                      'align': 'left',
#                      'font': {'family': 'Avenir LT Std 55 Roman',
#                               'size': '20px',
#                               'color': 'black'}
#                      },
#            'type': 'indicator',
#            'mode': 'gauge+number',
#            'value': valor_indice,
#            'align': 'center',
#            'number': {'font': {'family': 'Avenir LT Std 55 Roman',
#                                'size': '15px',
#                                'color': 'black'}
#                       },
#            'gauge': {'shape': 'angular',
#                      'bar': {'color': color_actual,
#                              'line': {'color': color_actual,
#                                       'width': '1'},
#                              'tickness': '1'},
#                      'bgcolor': 'white',
#                      'bordercolor': 'black',
#                      'borderwidth': '1',
#                      'axis': {'range': [0, 500],
#                               'visible': True,
#                               'tickmode': 'array',
#                               'tickvals': marcas_indicador,
#                               'ticks': 'inside',
#                               'tickcolor': 'black',
#                               'ticklen': '10px'}
#                      }
#            }
#           ]
#
# layout_1 = {'title': 'Ahora'}
#
# figure_1 = {'data': data_1,
#             'layout': layout_1}
#
# # Indicador pronóstico
# data_2 = [{'title': {'text': leyenda_actual,
#                      'align': 'left',
#                      'font': {'family': 'Avenir LT Std 55 Roman',
#                               'size': '20px',
#                               'color': 'black'}
#                      },
#            'type': 'indicator',
#            'mode': 'gauge+number',
#            'value': valor_indice_pronostico,
#            'align': 'center',
#            'number': {'font': {'family': 'Avenir LT Std 55 Roman',
#                                'size': '15px',
#                                'color': 'black'}
#                       },
#            'gauge': {'shape': 'angular',
#                      'bar': {'color': color_actual,
#                              'line': {'color': color_actual,
#                                       'width': '1'},
#                              'tickness': '1'},
#                      'bgcolor': 'white',
#                      'bordercolor': 'black',
#                      'borderwidth': '1',
#                      'axis': {'range': [0, 500],
#                               'visible': True,
#                               'tickmode': 'array',
#                               'tickvals': marcas_indicador,
#                               'ticks': 'inside',
#                               'tickcolor': 'black',
#                               'ticklen': '10px'}
#                      }
#            }
#           ]
#
# layout_2 = {'title': 'Mañana'}
#
# figure_2 = {'data': data_2,
#             'layout': layout_2}

# ---------------------------------CONSTRUIR TABLA EXPLICATIVA DEL ÍNDICE DE CALIDA DEL AIRE------------------#

# Textos en celdas
buena = 'Existe poco o ningún riesgo para la salud. Se puede realizar cualquier actividad al aire libre'
regular = 'Los grupos susceptibles pueden presentar síntomas en la salud. Las personas que son extremadamente ' \
          'susceptibles a la contaminación deben considerar limitar la exposición al aire libre.'
mala = 'Los grupos susceptibles presentan efectos en la salud. Los niños, adultos mayores, personas con enfermedades ' \
       'respiratorias y cardiovasculares, así como personas que realizan actividad física al aire libre deben limitar ' \
       'la exposición al aire libre.'
m_mala = 'Todos pueden presentar efectos en la salud; quienes pertenecen a los grupos susceptibles experimentan' \
         ' efectos graves. Los niños, adultos mayores, personas que realizan actividad física intensa o con ' \
         'enfermedades respiratorias y cardiovasculares, deben evitar la exposición al aire libre mientras que ' \
         'el resto de la población debe limitar la exposición al aire libre.'
e_mala = 'Toda la población debe evitar la exposición al aire libre pues hay probabilidades de experimentar efectos graves en la salud.'
peligrosa = 'Toda la población experimenta efectos graves en la salud. Suspensión de actividades al aire libre.'

# Header y celdas
valores_header = ['Calidad del aire', 'Intervalo', 'Efectos en la salud y recomendaciones']
valores_celdas = [['Buena', 'Regular', 'Mala', 'Muy mala', 'Extremadamente mala', 'Peligrosa'],
                  ['0 - 50', '51 - 100', '101 - 150', '151 - 200', '201 - 300', '301 - 500'],
                  [buena, regular, mala, m_mala, e_mala, peligrosa]]

# Lista de colores con opacidades
lista_colores = ['#99ca3a', '#f7ec0f', '#f8991d', '#ed2124', '#7d287d', '#7e0230']
lista_colores_opacos = ['#cce29a', '#fbf4a3', '#ffc98b', '#f59678', '#b087b1', '#c77f93']
colores_columnas = [lista_colores, lista_colores_opacos]

data_tabla = go.Table(header={'values': valores_header,
                              'fill': {'color': '#ffffff'},
                              'font': {'family': 'Avenir LT Std 55 Roman',
                                       'size': 10,
                                       'color': 'black', },
                              'align': 'center'},
                      cells={'values': valores_celdas,
                             'font': {'family': 'Avenir LT Std 55 Roman',
                                      'size': 10,
                                      'color': 'black'},
                             'align': 'left',
                             'fill': {'color': colores_columnas}},
                      columnwidth=[18, 12, 70])

layout_tabla = {'title': 'Efectos en la salud'}

figure_tabla = {'data': [data_tabla],
                'layout': layout_tabla}

# ------------------------------------------CONSTRUIR LAYOUT DE LA PÁGINA----------------------------------------------#

estilo_graficas = {'responsive': True,
                   'autosizable': True,
                   'displaylogo': False}

# layout= html.Div([dcc.Graph(id='indices', figure=figure_lineas, animate=True, className='indices', config=estilo_graficas),
#                   dcc.Graph(id='indicador_1', figure=figure_1, className='indicador_1', config=estilo_graficas),
#                   dcc.Graph(id='tabla', figure= figure_tabla, className='tabla')], className='contenedor-pronostico')


layout = html.Div(
    [html.Div(dcc.Graph(figure=figure_mapa, id='mapa-graph', className='mapa-graph', config=estilo_graficas),
              id='mapa', className='mapa'),
     html.Div([html.P('Indice de contaminación'),
               html.H1(id='indice', className='indice')], id='indicador', className='mini_container-grid-2'),
     dcc.Graph(id='tabla', figure=figure_tabla, className='tabla'),
     dcc.Graph(id='indices', figure=figure_lineas, animate=True, className='indices', config=estilo_graficas)],
    className='contenedor-pronostico')
