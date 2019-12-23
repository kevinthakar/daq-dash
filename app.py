import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random
from puller import getvalue
#from pandas_datareader.data import DataReader
#from max6675 import tc1
#print(dict_temp)
app = dash.Dash('data-logger')
app.title = 'Citriot'
max_length = 50
times = deque(maxlen=max_length)
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

times = deque(maxlen=max_length)

thermocouple_1 = deque([1,2,3,4,5,6,7,8,9,10])
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


def update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values

        thermocouple_1.append(1)
        thermocouple_2.append(20)
        thermocouple_3.append(30)
        thermocouple_4.append(40)
        thermocouple_5.append(50)
        thermocouple_6.append(60)
        thermocouple_7.append(70)
        thermocouple_8.append(80)
    else:
        for data_of_interest in [thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8]:
            pass#data_of_interest.append(data_of_interest[-1]+data_of_interest[-1])

    return times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8

    times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8 = update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)
    print(times)
 

def update_accelerometer_sensor(times, accelerometer_1, accelerometer_2, accelerometer_3):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        accelerometer_1.append(100)
        accelerometer_2.append(200)
        accelerometer_3.append(300)

    else:
        for data_of_interest in [accelerometer_1, accelerometer_2, accelerometer_3]:
            pass#data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, accelerometer_1, accelerometer_2, accelerometer_3


    times, accelerometer_1, accelerometer_2, accelerometer_3, accelerometer_4, accelerometer_5, accelerometer_6, accelerometer_7, accelerometer_8 = update_thermocouple_sensor(times, accelerometer_1, accelerometer_2, accelerometer_3, accelerometer_4, accelerometer_5, accelerometer_6, accelerometer_7, accelerometer_8)


def analog_digital_func():

    return 0

app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])


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
    ],)

])

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
        

@app.callback(dash.dependencies.Output('dropdownlist', 'options'),
              [dash.dependencies.Input('tabselect', 'value')])

def render_content(value):

    graphs = []
    if value == 'Thermocouple':
    
            return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]

    elif value == 'Accelerometer':

        return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]
    
    elif value == 'Analog/Digital/IO':

            return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]


@app.callback(dash.dependencies.Output('graphs', 'children'),
              [dash.dependencies.Input('dropdownlist', 'value'), dash.dependencies.Input('graph-update', 'n_intervals')])

def update_graph(data_names, n):

    graphs = []
    update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)
    update_accelerometer_sensor(times, accelerometer_1, accelerometer_2, accelerometer_3)

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
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(data_name))}
            )))

    return graphs





if __name__ == '__main__':
    app.run_server(debug=True)