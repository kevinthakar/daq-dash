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

def accelerometer_layout():
    
    X = html.Div([dcc.Interval(id="stream", interval=1000, n_intervals=0),
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

                html.Div(
                    html.Div(children=[

                        daq.Gauge(
                        id="x-gauge",
                        label="X-axis",
                        labelPosition="bottom",
                        units="g",
                        value=0,
                        min=-8,
                        max=8,
                        showCurrentValue=True
                    ),
                    daq.Gauge(
                        id="y-gauge",
                        label="Y-axis",
                        labelPosition="bottom",
                        units="g",
                        value=0,
                        min=-8,
                        max=8,
                        showCurrentValue=True
                    ),
                    daq.Gauge(
                        id="z-gauge",
                        label="Z-axis",
                        labelPosition="bottom",
                        units="g",
                        value=0,
                        min=-8,
                        max=8,
                        showCurrentValue=True
                    ),
                ],      style={'text-align':'center'}))])

    return X