import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random

app = dash.Dash('data-logger')
app.title = 'Citriot'

tab_style = {
    'borderBottom': '1px solid #d6d6d6',

    'fontWeight': 'bold',
    'backgroundColor': '#999999',
}

tabs_styles = {
    'height': '70px'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

max_length = 50
times = deque(maxlen=max_length)
oil_temps = deque(maxlen=max_length)
intake_temps = deque(maxlen=max_length)
coolant_temps = deque(maxlen=max_length)
rpms = deque(maxlen=max_length)
speeds = deque(maxlen=max_length)
throttle_pos = deque(maxlen=max_length)

data_dict = {"Oil Temperature":oil_temps,
"Intake Temperature": intake_temps,
"Coolant Temperature": coolant_temps,
"RPM":rpms,
"Speed":speeds,
"Throttle Position":throttle_pos}

########
thermocouple_1 = deque([1])
thermocouple_2 = deque([1,2,3,4,5,6,7,8,9,10])
thermocouple_3 = deque(maxlen=50)
thermocouple_4 = deque(maxlen=50)
thermocouple_5 = deque(maxlen=50)
thermocouple_6 = deque(maxlen=50)
thermocouple_7 = deque(maxlen=50)
thermocouple_8 = deque(maxlen=50)

accelerometer_1 = deque(maxlen=50)
accelerometer_2 = deque(maxlen=50)
accelerometer_3 = deque(maxlen=50)



data_thermocouple = {"Thermocouple 1": thermocouple_1,
"Thermocouple 2": thermocouple_2,
"Thermocouple 3": thermocouple_3,
"Thermocouple 4":thermocouple_4,
"Thermocouple 5":thermocouple_5,
"Thermocouple 6":thermocouple_6,
"Thermocouple 7":thermocouple_7,
"Thermocouple 8":thermocouple_8}


data_accelerometer =  {"Accelerometer 1": accelerometer_1,
"Accelerometer 2": accelerometer_2,
"Accelerometer 3": accelerometer_3}

tabs_corespondsensors = {'Thermocouple': ['Thermocouple 1', 'Thermocouple 2', 'Thermocouple 3',
                                            'Thermocouple 4', 'Thermocouple 5', 'Thermocouple 6',
                                         'Thermocouple 7', 'Thermocouple 8'],
                        'Accelerometer': ['Accelerometer 1', 'Accelerometer 2', 'Accelerometer 3']
                        }

names = list(tabs_corespondsensors.keys())

urange1, urange2, urange3, urange4, urange5, urange6, urange7, urange8 = 0,0,0,0,0,0,0,0 #integers
lrange1, lrange2, lrange3, lrange4, lrange5, lrange6, lrange7, lrange8 = 0,0,0,0,0,0,0,0 #integers
do1, do2, do3, do4, do5, do6, do7, do8 = 0,0,0,0,0,0,0,0 #Boolean Values
di1, di2, di3, di4, di5, di6, di7, di8 = 0,0,0,0,0,0,0,0 #Boolean Values


data_urange = {"urange1": urange1,
"urange2": urange2,
"urange3": urange3,
"urange4": urange4,
"urange5": urange5,
"urange6": urange6,
"urange7": urange7,
"urange8": urange8}

data_lrange = {"lrange":lrange1,
"lrange":lrange2,
"lrange":lrange3,
"lrange":lrange4,
"lrange":lrange5,
"lrange":lrange6,
"lrange":lrange7,
"lrange":lrange8,
}
data_di = {"di1": di1,
"di2": di2,
"di3": di3,
"di4": di4,
"di5": di5,
"di6": di6,
"di7": di7,
"di8": di8}

data_do = {"do1": do1,
"do2": do2,
"do3": do3,
"do4": do4,
"do5": do5,
"do6": do6,
"do7": do7,
"do8": do8}



def update_obd_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        thermocouple_1.append(random.randrange(180,230))
        thermocouple_2.append(random.randrange(95,115))
        thermocouple_3.append(random.randrange(170,220))
        thermocouple_4.append(random.randrange(1000,9500))
        thermocouple_5.append(random.randrange(30,140))
        thermocouple_6.append(random.randrange(10,90))
        thermocouple_7.append(random.randrange(35,90))
        thermocouple_8.append(random.randrange(10,90))
    else:
        for data_of_interest in [thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6

times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6 = update_obd_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6)



app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])

#app.layout = html.Div([
 #   html.Div([
  #      html.H2('Vehicle Data',
           #     style={'float': 'left',
  #                     }),
   #     ]),
    #dcc.Dropdown(id='vehicle-data-name',
     #            options=[{'label': s, 'value': s}
      #                    for s in data_thermocouple.keys()],
       #          value=['Thermocouple 1'],
        #         multi=True
         #        ),
    #html.Div(children=html.Div(id='graphs'), className='row'),
    #dcc.Interval(
     #   id='graph-update',
      #  interval=1000),
    #], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})
index_page = html.Div([

    html.Div([html.H3('Welcome to C-DAQ!')], style={'text-align':'center'}),
    html.Div([html.Img(src='assets/image2vector.svg')], style={'text-align':'center'}),
    html.Div([dcc.Link('Go to Digital Sensors', href='/page-1')], style={'text-align':'center'}),
    html.Br(),
    html.Div(dcc.Link('Go to Analog/Digital Inputs', href='/page-2'), style={'text-align':'center'}),
    ])

page_1_layout = html.Div([

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
            ])
        
        ]),
                    html.Div([
                        dcc.Tabs(id="tabselect", value=names[0], style=tab_style, children=[
                            dcc.Tab(label='Thermocouple', value=names[0], style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Accelerometer', value=names[1], style=tab_style, selected_style=tab_selected_style),
                                ],),
                        ]),

                    html.Div([dcc.Dropdown(id='dropdownlist',
                                value=['Thermocouple 1'],
                                multi=True),
                    ]),
                    html.Div(children=html.Div(id='graphs'), className='row'),
                    dcc.Interval(
                    id='graph-update',
                    interval=100),
                ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})

page_2_layout = html.Div([

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
            dcc.Link('Go back to home', href='/'),
    ]),

    html.Div(children=[#all three sections
        html.Div(children=[ #analog ip only
            html.H3('Analog Input'),

            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='Temp',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}
                )]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}
                ),
                ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]),
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                value='NYC',
                style={'width':'57%'}
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
                ])
            ]),

        html.Div(children=[html.H3("Digital Input"),
                daq.Indicator(
                id='my-toggle-switch',
                value=True,
                style={"marginBottom": 25},
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                label=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25}
        ),
                daq.Indicator(
                id='my-toggle-switch',
                value=False,
                style={"marginBottom": 25, 'text-align': 'center'}
        ),
            ], style={'width':'30%', 'marginLeft': 80, 'text-align': 'center', 'display':'inline-block '}),
    
        html.Div(children=[
            html.H3("Digital Output"),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
            daq.BooleanSwitch(
            id='my-daq-booleanswitch',
            on=True,
            style={'paddingBottom': 25}
        ),
        
    ], style={'width': '30%', 'text-align': 'center', 'display':'inline-block'}),
    ]),

])


@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('vehicle-data-name', 'value'), dash.dependencies.Input('graph-update', 'interval')]
    )
def update_graph(data_names, n):
    graphs = []
    update_obd_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6)
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




if __name__ == '__main__':
    app.run_server(debug=True)