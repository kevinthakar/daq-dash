import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random
import plotly.graph_objects as go


from variables import *
from components_layout import *

def digitalinput_tab():
    X = html.Div(children=[

        html.Div(
                        id="banner",
                        className="banner",
                        children=[

                        html.Div(
                        id="banner-text",
                        children=[
                            html.H5("Data Acquisition Metrics"),
                        ]),

                html.Div(
                    id="about-us-button",
                    children=[
                    html.Div(
                    children=[
                        html.H5(children="Citriot Solutions", n_clicks=0),
                        html.H6(children="Think. Engineer.", n_clicks=0),
                        ]),
                html.Img(src='assets/citriot_logo.jpg')
            ]),
dcc.Link(html.Button('Go back to home', style={'backgroundColor':'white'}), href='/'),        
            ]),
        
        html.H3("Digital Input", style={'text-align':'center'}), #element 1
                
        html.Div([
            daq.Indicator(
                id='my-toggle-switch-1',
                value=0,
                color='#ff0000',
                label="DI 1",
                style={"marginBottom": 25},
                ),#element 2

                daq.Indicator(
                id='my-toggle-switch-2',
                value=0,
                color='#ff0000',
                label="DI 2",
                style={"marginBottom": 25}
                ), #element 3

                daq.Indicator(
                id='my-toggle-switch-3',
                value=True,
                color='#ff0000',
                label="DI 3",
                style={"marginBottom": 25}
                ), #element 4

                daq.Indicator(
                id='my-toggle-switch-4',
                value=True,
                color='#ff0000',
                label="DI 4",
                style={"marginBottom": 25}
                ), #element 5
                daq.Indicator(
                id='my-toggle-switch-5',
                value=True,
                color='#ff0000',
                label="DI 5",
                style={"marginBottom": 25}
                ), #element 6
                daq.Indicator(
                id='my-toggle-switch-6',
                value=True,
                label="DI 6",
                color='#ff0000',
                style={"marginBottom": 25}
                ), #element 7
                daq.Indicator(
                id='my-toggle-switch-7',
                value=True,
                color='#ff0000',
                label="DI 7",
                style={"marginBottom": 25}
                ), #element 8
                daq.Indicator(
                id='my-toggle-switch-8',
                value=True,
                color='#ff0000',
                label="DI 8",
                style={"marginBottom": 25, 'text-align': 'center'}
                )
            ]), #element 9
            ])
    return X
