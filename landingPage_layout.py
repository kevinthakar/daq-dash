import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from variables import *
from thermocouple_layout import *
from accelerometer_layout import *
from analogInput_layout import *
from digitalInput_layout import *
from digitalOutput_layout import *

def landing_layout():

    X =  html.Div(children=[

    html.Div([html.Div([html.H3('Welcome to Portable C-DAQ!')], style={'text-align':'center'}),
    html.Br(),
    html.Div([html.Img(src='assets/image2vector (1).svg', style={'width':'15%'})], style={'text-align':'center'}),
    html.Br()]),

    html.Div([dcc.Link(html.Button('Go to Temperature Sensors', style={'backgroundColor':'white'}), href='/page-1'), dcc.Link(html.Button('Go to Thermocouple Readings', style={'backgroundColor':'white'}), href='/page-6'), dcc.Link(html.Button('Go to Accelerometer Sensors',  style={'backgroundColor':'white'}), href='/page-2')], style={'text-align':'center'}),
    html.Br(),
    html.Br(),
    html.Div([dcc.Link(html.Button('Go to Analog Input Sensors (AI)', style={'backgroundColor':'white'}), href='/page-3'),dcc.Link(html.Button('Go to Analog Sensor Readings', style={'backgroundColor':'white'}), href='/page-7'), dcc.Link(html.Button('Go to Digital Input Sensors (DI)', style={'backgroundColor':'white'}), href='/page-4'), dcc.Link(html.Button('Go to Digital Output Sensors (DO)', style={'backgroundColor':'white'}), href='/page-5')], style={'text-align':'center'})
])

    return X