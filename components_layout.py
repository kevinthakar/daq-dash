#!/home/pi/MyDAQApp/daq/bin/python3
#import RPi.GPIO as GPIO
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
from landingPage_layout import *


app = dash.Dash('data-logger', external_stylesheets=external_css)
app.title = 'Citriot'
app.config['suppress_callback_exceptions'] = True

external_css = ["https://codepen.io/chriddyp/pen/bWLwgP.css",
                "https://cdn.rawgit.com/samisahn/dash-app-stylesheets/" +
                "0925c314/dash-accelerometer.css",
                "https://fonts.googleapis.com/css?family=Dosis"]


app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])


index_page = html.Div([landing_layout()])
page_1_layout = html.Div([thermocouple_layout()])
page_2_layout = html.Div([accelerometer_layout()])
page_3_layout = html.Div(analog_tab())
page_4_layout = html.Div(digitalinput_tab())
page_5_layout = html.Div(digitaloutput_tab())
page_6_layout = html.Div(thermocouple_readings())
page_7_layout = html.Div(show_analog_tab())
