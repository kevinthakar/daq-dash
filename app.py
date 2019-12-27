#!/home/pi/MyDAQApp/daq/bin/python3

#import Adafruit_ADS1x15
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
from update_readings import *

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
    [dash.dependencies.Input('dropdownlist2', 'value'), dash.dependencies.Input('graph-update', 'interval')]
    )
def display_accel(data_names, n):

    graphs = []
    update_accelerometer_values(times, accelerometer_1, accelerometer_2, accelerometer_3)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for data_name in data_names:

        data = go.Scatter(
            x=list(times),
            y=list(data_accelerometer[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_accelerometer[data_name]),max(data_accelerometer[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':70},
                                                        title='{}'.format(data_name))}
            ), className=class_choice))

    return graphs
    
if __name__ == '__main__':
    app.run_server(debug=True)
