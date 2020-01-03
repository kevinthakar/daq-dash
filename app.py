#!/home/pi/MyDAQApp/daq/bin/python3

import Adafruit_ADS1x15
import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random
import plotly.graph_objects as go
import RPi.GPIO as GPIO
from thermocouple import temp_data
from Accelerometer import accelerometer_values
from variables import *
from components_layout import *
from update_readings import *

pinList = [4,17,18,27,22,23,24,10]

GPIO.setmode(GPIO.BCM)

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
        if pathname == '/page-1':
            return page_1_layout
        elif pathname == '/page-2':
            return page_2_layout
        elif pathname == '/page-3':
            return page_3_layout
        elif pathname == '/page-4':
            return page_4_layout
        elif pathname == '/page-5':
            return page_5_layout
        elif pathname == '/page-6':
            return page_6_layout
        elif pathname == '/page-7':
            return page_7_layout
        else:
            return index_page



@app.callback(
    dash.dependencies.Output('graphop1','children'),
    [dash.dependencies.Input('dropdownlist1', 'value'), dash.dependencies.Input('graph-update', 'interval')]
    )
def update_graph(data_names, n):
    graphs = []
    list_value = []
        
    update_thermocouple_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for data_name in data_names:

        data = go.Scatter(
            x=list(times),
            y=list(data_thermocouple[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_thermocouple[data_name]),max(data_thermocouple[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':70},
                                                        title='{}'.format(data_name))}
            ), className=class_choice))

    return graphs


@app.callback(
    dash.dependencies.Output('posxyz','children'),
    [dash.dependencies.Input('dropdownlist2', 'value')]
    )
def display_accel(data_names):

    sensors = []
    x, y, z = accelerometer_values()
    #update_accelerometer_values(times, accelerometer_1, accelerometer_2, accelerometer_3)
    for data_name in data_names:

        sensors.append(daq.Gauge(
                    id="x-gauge",
                    label="X-axis",
                    labelPosition="bottom",
                    units="g",
                    value=x,
                    min=-8,
                    max=8,
                    showCurrentValue=True
                    ))

        sensors.append(daq.Gauge(
                    id="y-gauge",
                    label="Y-axis",
                    labelPosition="bottom",
                    units="g",
                    value=y,
                    min=-8,
                    max=8,
                    showCurrentValue=True
                    ))
        sensors.append(daq.Gauge(
                    id="z-gauge",
                    label="Z-axis",
                    labelPosition="bottom",
                    units="g",
                    value=z,
                    min=-8,
                    max=8,
                    showCurrentValue=True
                    ))

        print(data_name)
        print(sensors)

    return sensors

@app.callback(
    dash.dependencies.Output('x-gauge','value'),
    [dash.dependencies.Input('stream', 'n_intervals')]
    )
def stream(conn):
    if conn:
        x, y, z = accelerometer_values()
        return x



@app.callback(
    dash.dependencies.Output('toggle-switch-output-1', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-1', 'on')])

def update_output(on):
    if(on):
         GPIO.output(4, GPIO.HIGH)
    else:
        GPIO.output(4, GPIO.LOW)
        
    
    return 'The switch is {}.'.format(on)


@app.callback(
    dash.dependencies.Output('toggle-switch-output-2', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-2', 'on')])

def update_output(on):
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-3', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-3', 'on')])

def update_output(on):
    if(on):
         GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-4', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-4', 'on')])

def update_output(on):
    if(on):
         GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-5', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-5', 'on')])

def update_output(on):
    if(on):
         GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(27, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-6', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-6', 'on')])

def update_output(on):
    if(on):
         GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(22, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-7', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-7', 'on')])

def update_output(on):
    if(on):
         GPIO.output(23, GPIO.HIGH)
    else:
        GPIO.output(23, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

@app.callback(
    dash.dependencies.Output('toggle-switch-output-8', 'children'),
    [dash.dependencies.Input('my-daq-booleanswitch-8', 'on')])

def update_output(on):
    if(on):
         GPIO.output(24, GPIO.HIGH)
    else:
        GPIO.output(24, GPIO.LOW)
     
    return 'The switch is {}.'.format(on)

    
if __name__ == '__main__':
    app.run_server(debug=True)
