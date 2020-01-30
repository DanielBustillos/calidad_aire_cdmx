# _*_ coding: utf-8 _*_

"""Layout de la documentación para el público. Se da una breve explicación de la obtención del índice de calidad del
aire y de las concentraciones de los principales contaminantes. Así mismo también se explica el proceso que determina
el pronóstico de la calidad del aire en el Valle de México.
"""
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import locale

from datetime import timedelta

# Se establece el formato de hora local en español (México)
locale.setlocale(locale.LC_TIME, 'es_MX.utf8')

indice = 'Los contaminantes atmosféricos son toda sustancia que al entrar en contacto con la atmósfera, altera la ' \
         'condición natural de la misma. Según la Norma Ambiental para la Ciudad de México publicada en 2017 se ' \
         'consideran seis contaminantes criterios, que afectan la salud y bienestar de la población. Estos ' \
         'contaminantes son el ozono (O\u2083), dióxido de azufre (SO\u2082), monóxido de carbono (CO), dióxido ' \
         'de nitrógeno (NO\u2082), partículas menores a 10 micrómetros (PM\u2081\u2080), y menores a 2.5 micrómetros ' \
         '(PM\u2082\u002e\u2085)'

# ------------------------------------------CONSTRUIR LAYOUT DE LA PÁGINA----------------------------------------------#

layout = html.Div(
    [html.Div([html.H2('Índice de Calidad del Aire'),
               html.P(indice)], id='indice', className='indice')])