import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random
#import Adafruit_ADS1x15

times = deque(maxlen=50)
thermocouple_1 = deque(maxlen=50)
thermocouple_2 = deque(maxlen=50)
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
 
app = dash.Dash('data-logger')
app.title = 'Citriot'

app.config['suppress_callback_exceptions'] = True

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

def analog_digital_func(times, data_lrange, data_urange, data_di, data_do):

    #upper = 1345
    #lower = 25

    #adc = Adafruit_ADS1x15.ADS1115()
    #adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
    #value1=adc.read_adc(0,gain=1)
    #value1=((value1/32768.0)*4.096*10)
    #value1=(((value1-4)/16)*(upper-lower))+ lower #Converting current to temperature through slope curve method
    #press = round(value1, 5)
    return 0


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
            dcc.Link('Go back to home', href='/'),
        
            ]),
        html.Div([html.H3('Analog Input')], style={'text-align':'center'}), #element1
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
                )]), #element 2
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
                ]), #element 3
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
            ]), #element 4
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
            ]), #element 5
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
                    ],
                value='NYC',
                style={'width':'57%'}),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                style={'paddingBottom': 30, 'display':'inline-block'}),
            ]), #element 6
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
            ]), #element 7
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
            ]), #element 8
            html.Div([
                dcc.Dropdown(
                id='demo-dropdown',
                options=[
                    {'label': 'Pressure', 'value': 'Temp'},
                    {'label': 'Vibration', 'value': 'Vib'},
                    {'label': 'Flow', 'value': 'Flow'}
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
                ]) #element 9
            ])

    return X

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
            dcc.Link('Go back to home', href='/'),
        
            ]),
        
        html.H3("Digital Input", style={'text-align':'center'}), #element 1
                
        html.Div([
            daq.Indicator(
                id='my-toggle-switch-1',
                value=True,
                color='#ff0000',
                label="DI 1",
                style={"marginBottom": 25},
                ),#element 2

                daq.Indicator(
                id='my-toggle-switch-2',
                value=True,
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
            dcc.Link('Go back to home', href='/'),
        
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

app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])


index_page = html.Div(children=[

    html.Div([html.Div([html.H3('Welcome to Portable C-DAQ!')], style={'text-align':'center'}),
    html.Br(),
    html.Div([html.Img(src='assets/image2vector (1).svg')], style={'text-align':'center'}),
    html.Br()]),

    html.Div([dcc.Link(html.Button('Go to Temperature Sensors', style={'backgroundColor':'white'}), href='/page-1'), dcc.Link(html.Button('Go to Thermocouple Sensors',  style={'backgroundColor':'white'}), href='/page-2')], style={'text-align':'center'}),
    html.Br(),
    html.Br(),
    html.Div([dcc.Link(html.Button('Go to Analog Input Sensors', style={'backgroundColor':'white'}), href='/page-3'), dcc.Link(html.Button('Go to Digital Input Sensors', style={'backgroundColor':'white'}), href='/page-4'), dcc.Link(html.Button('Go to Digital Output Sensors', style={'backgroundColor':'white'}), href='/page-5')], style={'text-align':'center'})
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
            ]),
            dcc.Link('Go back to home', href='/'),
        
            ]),
                html.Div([dcc.Dropdown(id='dropdownlist1',
                                options = [{'label': s, 'value': s} for s in data_thermocouple.keys()],
                                value=['Thermocouple 1'],
                                multi=True),
                    ]),
                    html.Div(children=[html.Div(id='graphop1')], className='row'),
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
            dcc.Link(html.Button('Go back to home'), href='/'),
        
            ]),
                html.Div([dcc.Dropdown(id='dropdownlist2',
                                options = [{'label': s, 'value': s} for s in data_accelerometer.keys()],
                                value=['Accelerometer 1'],
                                multi=True),
                    ]),
                    html.Div(children=html.Div(id='posxyz'), className='row'),
                ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


page_3_layout = html.Div(analog_tab())
page_4_layout = html.Div(digitalinput_tab())
page_5_layout = html.Div(digitaloutput_tab())




def update_thermocouple_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8):

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

    return times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8

times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8 = update_thermocouple_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)

def update_accelerometer_values(times, accelerometer_1, accelerometer_2, accelerometer_3):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        accelerometer_1.append(random.randrange(10,90))
        accelerometer_2.append(random.randrange(35,90))
        accelerometer_3.append(random.randrange(10,90))
    else:
        for data_of_interest in [accelerometer_1, accelerometer_2, accelerometer_3]:
            pass#data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, accelerometer_1, accelerometer_2, accelerometer_3

times, accelerometer_1, accelerometer_2, accelerometer_3 = update_accelerometer_values(times, accelerometer_1, accelerometer_2, accelerometer_3)


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

    return html.Div([
            html.Div([
                html.H3("G-Force")
            ], className='Title'),
            html.Div([
                html.Div([
                    html.Div(
                        "X-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="x-value",
                        className="one columns",
                        style={'marginRight': '20px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "Y-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="y-value",
                        className="one columns",
                        style={'marginRight': '20px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "Z-axis:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="z-value",
                        className="one columns",
                        style={'marginRight': '20px'}),
                    html.Div(
                        "g",
                        className="one columns")
                ], className="row"),
                html.Div([
                    html.Div(
                        "Time Stamp:",
                        style={'textAlign': 'right'},
                        className="three columns"),
                    html.Div(
                        id="time-stamp",
                        className="one columns",
                        style={'marginRight': '10px'}),
                    html.Div(
                        "s",
                        className="one columns")
                ], className="row"),
            ]),
        ], className="six columns")





if __name__ == '__main__':
    app.run_server(debug=True)