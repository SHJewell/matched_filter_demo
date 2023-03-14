import dash
from dash import html as dhtml
from dash import dcc, Input, Output, State
from dash.dash_table.Format import Format, Scheme
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import dash_bootstrap_components as dbc

#non-plotly imports
import numpy as np
import pandas as pd

'''
========================================================================================================================
Dashboard

There are two options for mapping: using the mapping functions in Plotly, but these are slow

And using a heatmap, which is fast. Maybe giving the user the option to switch between these would be good?
'''

graph_config = {'modeBarButtonsToRemove' : ['hoverCompareCartesian', 'select2d', 'lasso2d'],
                'doubleClick':  'reset+autosize', 'toImageButtonOptions': { 'height': None, 'width': None, },
                'displaylogo': False}

colors = {'background': '#111111', 'text': '#7FDBFF'}

app = dash.Dash(__name__,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                external_stylesheets=[dbc.themes.SLATE])
#application = app.server
app.title = "Matched Filter Dashboard"

filter_card = dhtml.Div([
    dhtml.H5('Matched Filter'),
    make_subplots(rows=2, cols=1,
                  subplot_titles=['Time Lag', 'Deconvolution'])
    ]
)

controls_tab = dhtml.Div([
    dhtml.H5('Noise'),
    dcc.Slider(id='additive-noise', max=1, min=0, value=1),
    dhtml.H5('Time Lag'),
    dcc.Slider(id='t-lag', max=1, min=0, value=0),
    ]
)

input_plots = make_subplots(rows=2, cols=1, subplot_titles=['Raw Signal', 'Filtering Signal'])
input_plots.update_layout(paper_bgcolor='#515960', plot_bgcolor='#515960',
                  font_color='white',
                  margin=dict(l=10, r=10, t=10, b=10))

out_plots = make_subplots(rows=2, cols=1, subplot_titles=['Time Lag', 'Deconvolution'])
out_plots.update_layout(paper_bgcolor='#515960', plot_bgcolor='#515960',
                  font_color='white',
                  margin=dict(l=10, r=10, t=10, b=10))

app.layout = dhtml.Div([
    dbc.Card(
        dbc.CardBody(
            dbc.Row(
                children=[
                    dbc.Col(width=4, children=[dcc.Loading(dcc.Graph(id='input-series', figure=input_plots))]),
                    dbc.Col(width=4, children=[dcc.Loading(dcc.Graph(id='out-series', figure=out_plots))]),
                    dbc.Col(width=4, children=[controls_tab])
                ]
            )
        )
    ),
    dcc.Link('By SHJewell', href=f'https://shjewell.com'),
    dhtml.H6(f'Built using Python and Plotly Dash'),
    dcc.Link('Source code', href=f'https://github.com/SHJewell/wait_five_minutes_weather')
])

'''
========================================================================================================================
Callbacks
'''

# @app.callback(
#     [Output('mapbox', 'figure'),
#      Output('map-label', 'children')],
#     [Input('set-select', 'value'),
#      Input('analysis-select', 'value')]
# )
# def update_map(set, analysis):
#     pass

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
    #application.run(port=8080)
