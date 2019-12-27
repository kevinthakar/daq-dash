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

def analog_tab():
    
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
        html.Div([html.H3('Analog Input')], style={'text-align':'center'}), #element1
            html.Div([
                html.Div([
                    dcc.Dropdown(
                    id='dropdown-1',
                    options=[
                        {'label': 'Pressure', 'value': 'Temp'},
                        {'label': 'Vibration', 'value': 'Vib'},
                        {'label': 'Flow', 'value': 'Flow'}
                        ],
                    value='Temp',
                    style={'width':'57%'}),
                    daq.NumericInput(
                    id='my-numeric-input-11',
                    value=0,
                    label='AI 1 Upper Range',
                    style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                    ),
                    daq.NumericInput(
                    id='my-numeric-input-12',
                    value=0,
                    label='AI 1 Lower Range',
                    style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
                    )]), #element 2
            html.Div([
                dcc.Dropdown(
                id='dropdown-2',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-21',
                value=0,
                label='AI 2 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}                ),
                daq.NumericInput(
                id='my-numeric-input-22',
                value=0,
                label='AI 2 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
                ),
                ]), #element 3
            html.Div([
                dcc.Dropdown(
                id='dropdown-3',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-31',
                label='AI 3 Upper Range',
                value=0,
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
                ),
                daq.NumericInput(
                id='my-numeric-input-32',
                value=0,
                label='AI 3 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
            ]), #element 4
            html.Div([
                dcc.Dropdown(
                id='dropdown-4',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-41',
                value=0,
                label='AI 4 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input-42',
                value=0,
                label='AI 4 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
            ]), #element 5
            html.Div([
                dcc.Dropdown(
                id='dropdown-5',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-51',
                value=0,
                label='AI 5 Upper Range',
                style={'paddingBottom': 30,  'paddingTop':30, 'display':'inline-block' }
                ),
                daq.NumericInput(
                id='my-numeric-input-52',
                value=0,
                label='AI 5 Lower Range',
                style={'paddingBottom': 30,  'paddingTop':30, 'display':'inline-block'}),
            ]), #element 6
            html.Div([
                dcc.Dropdown(
                id='dropdown-6',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-61',
                value=0,
                label='AI 6 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input-62',
                value=0,
                label='AI 6 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
            ]), #element 7
            html.Div([
                dcc.Dropdown(
                id='dropdown-7',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input-71',
                value=0,
                label='AI 7 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input-72',
                value=0,
                label='AI 7 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
            ]), #element 8
            html.Div([
                dcc.Dropdown(
                id='dropdown-8',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}
                ),
                daq.NumericInput(
                id='my-numeric-input-81',
                value=0,
                label='AI 8 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input-82',
                value=0,
                label='AI 8 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
                ])
             ],) #element 9
            ])

    return X

def show_analog_tab():

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
    html.H3('Analog Input Readings', style={'text-align':'center'}),
    daq.LEDDisplay(
    label="AI-1",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-2",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-3",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-4",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-5",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-6",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-7",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI-8",
    labelPosition='top',
    value='12:34')
    
      ])
    return X