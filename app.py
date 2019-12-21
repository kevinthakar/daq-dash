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

listoflist_th = []
a_list = []
listoflist_th.append(a_list)

thermocouple_1 = deque(maxlen=max_length)
thermocouple_2 = deque(maxlen=max_length)
thermocouple_3 = deque(maxlen=max_length)
thermocouple_4 = deque(maxlen=max_length)
thermocouple_5 = deque(maxlen=max_length)
thermocouple_6 = deque(maxlen=max_length)
thermocouple_7 = deque(maxlen=max_length)
thermocouple_8 = deque(maxlen=max_length)

accelerometer_1 = deque(maxlen=max_length)
accelerometer_2 = deque(maxlen=max_length)
accelerometer_3 = deque(maxlen=max_length)


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

dict_temp = {}
temp = ''
vib = ''
flow = ''
Urange = 0
Lrange = 0
#dict_temp = tc1()

data_analog = "Temperature"

metadata_third = {"Temperature": temp,
"Vibration": vib,
"Flow": flow}

metadata_range = {"Upper Range": Urange,
"Lower Range": Lrange}

#temp, vibration, flow = getvalue()
tabs_corespondsensors = {'Thermocouple': ['Thermocouple 1', 'Thermocouple 2', 'Thermocouple 3',
                                            'Thermocouple 4', 'Thermocouple 5', 'Thermocouple 6',
                                         'Thermocouple 7', 'Thermocouple 8'],
                        'Accelerometer': ['Accelerometer 1', 'Accelerometer 2', 'Accelerometer 3'],
                        'Analog/Digital/IO': ['hello', 'world']
                        }

names = list(tabs_corespondsensors.keys())
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0


data_pins =  {"Analog 1": a1,
"Analog 2": a2,
"Analog 3": a3,
"Analog 4": a4,
"Analog 5": a5,
"Analog 6": a6,
"Analog 7": a7,
"Analog 8": a8 }

data_di = {"di_1": 0,
"di_2": 0,
"di_3": 0,
"di_4": 0,
"di_5": 0,
"di_6": 0,
"di_7": 0,
"di_8": 0,}

data_do = {"do_1": 0,
"do_2": 0,
"do_3": 0,
"do_4": 0,
"do_5": 0,
"do_6": 0,
"do_7": 0,
"do_8": 0}

data_sensors = []
s = []

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1', ),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Img(src='assets/citriot_logo (2).svg')])

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
                        dcc.Tabs(id="input-source-1", value=names[0], style=tab_style, children=[
                            dcc.Tab(label='Thermocouple', value=names[0], style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Accelerometer', value=names[1], style=tab_style, selected_style=tab_selected_style),
                                ],),
                        ]),

                    html.Div(id= 'output-source-11', children=
                            dcc.Dropdown(id='output-source-1',
                                #value=['Accelerometer 1'],
                                multi=True),
                            ),

                    html.Div(id='output-source-22',children=[
                            dcc.Graph(id='output-source-2'),
                            dcc.Interval(
                                    id='graph-update',
                                    interval=1000)],
                            className="container",style={'width':'100%','max-width':50000})
])


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
        
def update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        thermocouple_1.append(random.randrange(180,230))
        thermocouple_2.append(random.randrange(95,115))
        thermocouple_3.append(random.randrange(170,220))
        thermocouple_4.append(random.randrange(1000,9500))
        thermocouple_5.append(random.randrange(30,140))
        thermocouple_6.append(random.randrange(10,90))
    else:
        for data_of_interest in [thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8

    times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8 = update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)
 

def update_accelerometer_sensor(times, accelerometer_1, accelerometer_2, accelerometer_3):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        accelerometer_1.append(random.randrange(180,230))
        accelerometer_2.append(random.randrange(95,115))
        accelerometer_3.append(random.randrange(170,220))

    else:
        for data_of_interest in [accelerometer_1, accelerometer_2, accelerometer_3]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, accelerometer_1, accelerometer_2, accelerometer_3


    times, accelerometer_1, accelerometer_2, accelerometer_3, accelerometer_4, accelerometer_5, accelerometer_6, accelerometer_7, accelerometer_8 = update_thermocouple_sensor(times, accelerometer_1, accelerometer_2, accelerometer_3, accelerometer_4, accelerometer_5, accelerometer_6, accelerometer_7, accelerometer_8)


def analog_digital_func():
    return 0

# times, acc1, acc2... = update 
#times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6 = update_thermocouple_sensor(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6)

@app.callback(dash.dependencies.Output('output-source-1', 'options'),
              [dash.dependencies.Input('input-source-1', 'value')])

def render_content(value):

    graphs = []
    if value == 'Thermocouple':
    
            return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]

    elif value == 'Accelerometer':

        return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]
    
    elif value == 'Analog/Digital/IO':

            return [{'label': i, 'value': i} for i in tabs_corespondsensors[value]]

@app.callback(dash.dependencies.Output('output-source-2', 'children'),
              [dash.dependencies.Input('output-source-1', 'value')])

def render_content(value):

    th_no = value
    graphs = []

    data = go.Scatter(
            x=list(times),
            y=list(data_thermocouple[value]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

    graphs.append(html.Div(dcc.Graph(
            id=value,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_thermocouple.get(value)),max(data_thermocouple.get(value))]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(value))}
            )))

    return graphs





if __name__ == '__main__':
    app.run_server(debug=True)