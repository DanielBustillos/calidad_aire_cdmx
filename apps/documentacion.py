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

indice1 ='Los contaminantes atmosféricos son toda sustancia que al entrar en contacto con la atmósfera, altera la ' \
         'condición natural de la misma. Según la Norma Ambiental para la Ciudad de México\u00b9 publicada en 2017 se '\
         'consideran seis contaminantes criterios, que afectan la salud y bienestar de la población. Estos ' \
         'contaminantes son el ozono (O\u2083), dióxido de azufre (SO\u2082), monóxido de carbono (CO), dióxido ' \
         'de nitrógeno (NO\u2082), partículas suspendidas menores a 10 micrómetros (PM\u2081\u2080), y menores ' \
         'a 2.5 micrómetros (PM\u2082\u002e\u2085). Las estaciones de monitoreo situadas a lo largo del Valle ' \
         'de México (mapa en el tablero de pronóstico) miden las concentraciones de estos contaminantes hora a hora ' \
         'generando así una base de datos con la que es posible calcular el índice de calidad del aire. Para el ' \
         'ozono, monóxido de carbono, dióxido de nitrógeno y dióxido de azufre, la concentración está dada en ' \
         'partes por millón (ppm), mientras que para las partículas suspendidas está dada en microgramos ' \
         'por metro cúbico (\u03BCg/m\u00B3). Los métodos por los cuales se hacen estas mediciones están descritos ' \
         'en las Normas oficiales Mexicanas\u00b9.'

indice2 ='Según las mismas normas oficiales, el índice de calidad del aire se calcula de acuerdo al contaminante ' \
         'criterio. Para el ozono y el dióxido de nitrógeno se usan las concentraciones promedio de una hora; para ' \
         'el dióxido de azufre la concentración como un promedio móvil de 24 horas; para el monóxido de carbono ' \
         'la concentración obtenida como un promedio móvil de 8 horas; y por último para las partículas suspendidas ' \
         'como un promedio móvil de 24 horas. Con estos datos, se usa un algoritmo establecido en la Norma Ambiental ' \
         'para la Ciudad de México\u00b9 para calcular el índice de calidad del aire. El índice reportado en este ' \
         'tablero es aquel del contaminante atmosférico de mayor magnitud en las estaciones de monitoreo.'

indice3 ='De acuerdo a la magnitud del índice de calidad del aire se clasifican los riesgos a la población y se ' \
         'comunican con un código de colores universal, que es la tabla que se puede ver en el tablero.' \

indice4 ='La metodología del cálculo del índice de calidad del aire y mucha más información se puede encontrar en la ' \
         'página de la Secretaría del Medio Ambiente de la Ciudad de México\u00B2.'

pronostico1 ='bla bla Dan'

pronostico2 ='bla bla Dan'

referencia1 = 'http://www.aire.cdmx.gob.mx/descargas/monitoreo/normatividad/NADF-009-AIRE-2017.pdf'

referencia2 = 'https://www.sedema.cdmx.gob.mx/'
#
# referencia3 =

# ------------------------------------------CONSTRUIR LAYOUT DE LA PÁGINA----------------------------------------------#

layout = html.Div(
    [html.Div([html.H3('Índice de Calidad del Aire'),
               html.P(indice1),
               html.P(indice2),
               html.P(indice3),
               html.P(indice4)], id='documentacion-container', className='documentacion-container'),
     html.Div([html.H3('Pronóstico de Calidad del Aire'),
               html.P(pronostico1),
               html.P(pronostico2)], id='documentacion-container', className='documentacion-container'),
     html.Div([html.H4('Referencias'),
               html.P(dcc.Link('Norma Ambiental para el Distrito Federal NADF-008-AMBT-2017', href=referencia1)),
               html.P(dcc.Link('Secretaría del Medio Ambiente (SEDEMA)', href=referencia2))],
              id='documentacion-container', className='documentacion-container')
     ])