# App de concentraciones de contaminantes (PM10 y O3)

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import locale

from datetime import timedelta

# Funciones y datos necesarios
from common.conversion_indice import convertir_ppb
from common.diccionarios import dic_etiquetas, dic_colores
from data.db_conexion import df

# Se establece el formato de hora local en español (México)
locale.setlocale(locale.LC_TIME, 'es_MX.utf8')

# Se definen las funciones de diccionarios como variables
dic_etiquetas = dic_etiquetas()
dic_colores = dic_colores()

# Se lee el archivo original
# df = pd.read_csv('viz_aire_cdmx/data/datos_d.csv', error_bad_lines=False, parse_dates=['fecha'])

# Se establece el rango de fechas (7 días antes de la predicción) y se estructura el dataframe
fecha_max = max(df['fecha'])
fecha_min = min(df['fecha'])
inicio_rango = fecha_max - timedelta(days=7)
fecha_actual = fecha_max - timedelta(days=1)

mask= (df['fecha']>=inicio_rango) & (df['fecha']<=fecha_actual)
df= df.loc[mask]

# Se convierten las unidades de PM10 a partículas por billón (ppb)
# df['pm10mean_max_ppb'] = df.apply(lambda row: convertir_ppb(row, 'pm10mean_max'), axis=1)
# df.reset_index(inplace=True, drop=True)

# Se eligen sólo las columnas necesarias para graficar y se redondea el df a 2 decimales
df = df[['fecha', 'pm10mean_max', 'o3_max']]

# Función que crea cada trazo, es decir una línea por contaminante y define si es sólida o punteada
def crear_bar_chart(df, y, name, color, x='fecha'):
    trazo = go.Bar(x=df[x],
                   y=df[y],
                   name=name,
                   marker_color=color)
    return trazo


# Datos y configuración de la figura para graficar usando layout de dash
data = [crear_bar_chart(df, col, dic_etiquetas[col], dic_colores[col]) for col in df.columns[1:]]
figure ={'data': data,
        'layout': go.Layout(xaxis={'title': 'fecha',
                                   'tickangle': -45,
                                   'automargin': True,
                                   'tickformat': '%d %B / %H hrs',
                                   'showgrid': False,
                                   'nticks': 22},
                            yaxis={'title': '\u03BCg/m\u00B3 (PM10) / ppb (O3)',
                                   'range': [0, 200],
                                   'showgrid':False,
                                   'showticklabels': True,
                                   'showline': False},)
        }


# Configuración del layout de dash para esta gráfica
layout = html.Div([html.Div(dcc.Graph(id='concentraciones',
                                      figure=figure), className='contenedor-concentraciones'),
                   html.Div(html.P(
                       'Los valores reportados para la concentración de los contaminantes PM10 y O3 son los máximos '
                       'reportados por hora de todas las estaciones existentes en el Valle de México.'),
                            className='grid-item'),
                   dcc.Interval(id= 'concentraciones-update',
                                interval=1*500)
                   ])