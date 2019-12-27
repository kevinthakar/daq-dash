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


def digitaloutput_tab():

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
                    html.H3("Digital Output", style={'text-align':'center'}),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-1',
                    on=True,
                    label='DO 1',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-2',
                    on=True,
                    label='DO 2',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-3',
                    on=True,
                    label='DO 3',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-4',
                    on=True,
                    label='DO 4',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-5',
                    on=True,
                    label='DO 5',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-6',
                    on=True,
                    label='DO 6',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-7',
                    on=True,
                    label='DO 7',
                    style={'paddingBottom': 25}
                ),
                    daq.BooleanSwitch(
                    id='my-daq-booleanswitch-8',
                    on=True,
                    label='DO 8',
                    style={'paddingBottom': 25}
                ),
                
            ], style={'text-a1ign': 'center'})
            
        return X