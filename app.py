import dash
import dash_html_components as html

from dash.dependencies import Input, Output
from apps import concentraciones, pronostico

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
        return pronostico.layout
    elif two > one and two > three:
        return concentraciones.layout
    elif three > two and three > one:
        return pronostico.layout
    else:
        return pronostico.layout


if __name__ == '__main__':
    app.run_server(debug=True)
