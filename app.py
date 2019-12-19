# _*_ coding: utf-8 _*_

"""Layout principal de la app de dash.

Este script construye el layout de la aplicación web del tablero de calidad del aire. Esta construido usando la
biblioteca de python DASH.

Hay dos aspectos fundamentales para construir esta aplicación web. Primeramente el usar un script de html (dentro de
este script de python) para poder personalizar algunos aspectos visuales de la misma (como el favicon). En segundo plano
el llamar a dos distintos módulos (tablero.py y documentacion.py) para mostrar a demanda aspectos diferentes del
tablero.
"""


import dash
import dash_html_components as html

from dash.dependencies import Input, Output
from apps import documentacion, tablero

# Se inicia a app en dash
app = dash.Dash(__name__)

# Se personaliza el template de html (head, footer, favicon, etc.)
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            body {
                margin: 0;
                font-family: "Avenir LT Std 55 Roman";
                font-size: 22px;
                # background-image: url('/assets/mapa_fondo.png');
                # background-position: center     center;
                # background-repeat: no-repeat;
                # background-attachment: fixed;
                # background-size: cover;
            }
        </style>
        <meta charset="UTF-8">
        <title>Calidad del aire CDMX</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
    </body>
</html>'''

# Con esto se construye el layout principal de la aplicación web.
app.layout = html.Div([html.Header([html.Div([html.Button([html.Div(className='bar1'),
                                                           html.Div(className='bar2'),
                                                           html.Div(className='bar3')],
                                                          id='myBtn', className='dropbtn'),
                                              html.Div([html.Button(html.Span('Pronóstico'), id='pronostico_button',
                                                                    n_clicks_timestamp=0, className='button'),
                                                        html.Button(html.Span('Concentraciones'),
                                                                    id='concentracion_button', n_clicks_timestamp=0,
                                                                    className='button'),
                                                        html.Button(html.Span('Documentación'),
                                                                    id='documentacion_button', n_clicks_timestamp=0,
                                                                    className='button')], id='myDropdown',
                                                       className='dropdown-content')], className='dropdown'),
                                    html.Div([html.H2('Calidad del aire CDMX')], id='titulo-app', className='titulo-app'),
                                    html.A([html.Img(src=app.get_asset_url('conacyt.png'),
                                                     alt="logo de conacyt", className='logo')],
                                           href='https://conacyt.gob.mx')]),
                       html.Div(id='contenido', className='contenedor-global')])


@app.callback(Output('contenido', 'children'),
              [Input('pronostico_button', 'n_clicks_timestamp'),
               Input('concentracion_button', 'n_clicks_timestamp'),
               Input('documentacion_button', 'n_clicks_timestamp')])
def on_click(one, two, three):
    if one > two and one > three:
        return tablero.layout
    elif two > one and two > three:
        return documentacion.layout
    elif three > two and three > one:
        return tablero.layout
    else:
        return tablero.layout


if __name__ == '__main__':
    app.run_server(debug=True)
