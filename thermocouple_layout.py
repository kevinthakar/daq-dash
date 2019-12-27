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


def show_values_tab():

    X = html.Div([

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
    html.H3('Thermocouple Values', style={'text-align':'center'}),
    daq.LEDDisplay(
    label="T 1 (Centigrade)",
    labelPosition='top',
    color='red',
    value='1.11'),

    daq.LEDDisplay(
    label="T 2 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 3 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 4 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 5 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 6 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 7 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 8 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34')
    
      ])
    return X