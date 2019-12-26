import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from variables import *

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

external_css = ["https://codepen.io/chriddyp/pen/bWLwgP.css",
                "https://cdn.rawgit.com/samisahn/dash-app-stylesheets/" +
                "0925c314/dash-accelerometer.css",
                "https://fonts.googleapis.com/css?family=Dosis"]


app = dash.Dash('data-logger', external_stylesheets=external_css)
app.title = 'Citriot'

app.config['suppress_callback_exceptions'] = True
val = 12.55

def show_values_tab():

    x = html.Div([

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
    html.H3('Thermocouple Values', style={'text-align':'center'}),
    daq.LEDDisplay(
    label="T 1 (Centigrade)",
    labelPosition='top',
    color='red',
    value=val),

    daq.LEDDisplay(
    label="T 2 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 3 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 4 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 5 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 6 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 7 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34'),

    daq.LEDDisplay(
    label="T 8 (Centigrade)",
    labelPosition='top',
    color='red',
    value='12.34')
    
      ])
    return x

def show_analog_tab():

    x = html.Div([

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
    html.H3('Thermocouple Values', style={'text-align':'center'}),
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
    label="AI 7",
    labelPosition='top',
    value='12:34'),

    daq.LEDDisplay(
    label="AI 8",
    labelPosition='top',
    value='12:34')
    
      ])
    return x

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
            dcc.Link(html.Button('Go back to home', style={'backgroundColor':'white'}), href='/'),
        
            ]),
        html.Div([html.H3('Analog Input')], style={'text-align':'center'}), #element1
            html.Div([
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
                    label='AI 1 Upper Range',
                    style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                    ),
                    daq.NumericInput(
                    id='my-numeric-input',
                    value=0,
                    label='AI 1 Lower Range',
                    style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
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
                label='AI 2 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 2 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
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
                label='AI 3 Upper Range',
                value=0,
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 3 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
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
                label='AI 4 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 4 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
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
                label='AI 5 Upper Range',
                style={'paddingBottom': 30,  'paddingTop':30, 'display':'inline-block' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 5 Lower Range',
                style={'paddingBottom': 30,  'paddingTop':30, 'display':'inline-block'}),
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
                label='AI 6 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 6 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
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
                label='AI 7 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 7 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
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
                label='AI 8 Upper Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block', 'paddingRight': '4%' }
                ),
                daq.NumericInput(
                id='my-numeric-input',
                value=0,
                label='AI 8 Lower Range',
                style={'paddingBottom': 30, 'paddingTop':30, 'display':'inline-block'}),
                ])
             ],) #element 9
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
dcc.Link(html.Button('Go back to home', style={'backgroundColor':'white'}), href='/'),        
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

app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])

a = 0

index_page = html.Div(children=[

    html.Div([html.Div([html.H3('Welcome to Portable C-DAQ!')], style={'text-align':'center'}),
    html.Br(),
    html.Div([html.Img(src='assets/image2vector (1).svg')], style={'text-align':'center'}),
    html.Br()]),

    html.Div([dcc.Link(html.Button('Go to Temperature Sensors', style={'backgroundColor':'white'}), href='/page-1'), dcc.Link(html.Button('Go to Thermocouple Readings', style={'backgroundColor':'white'}), href='/page-6'), dcc.Link(html.Button('Go to Accelerometer Sensors',  style={'backgroundColor':'white'}), href='/page-2')], style={'text-align':'center'}),
    html.Br(),
    html.Br(),
    html.Div([dcc.Link(html.Button('Go to Analog Input Sensors (AI)', style={'backgroundColor':'white'}), href='/page-3'),dcc.Link(html.Button('Go to Analog Sensor Readings', style={'backgroundColor':'white'}), href='/page-7'), dcc.Link(html.Button('Go to Digital Input Sensors (DI)', style={'backgroundColor':'white'}), href='/page-4'), dcc.Link(html.Button('Go to Digital Output Sensors (DO)', style={'backgroundColor':'white'}), href='/page-5')], style={'text-align':'center'})
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
dcc.Link(html.Button('Go back to home', style={'backgroundColor':'white'}), href='/'),        
            ]),
                html.Div([dcc.Dropdown(id='dropdownlist1',
                                options = [{'label': s, 'value': s} for s in data_thermocouple.keys()],
                                value=['Thermocouple 1'],
                                multi=True),
                    ]),
                    html.Div(children=[html.Div(id='graphop1'),], className='row'),
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
dcc.Link(html.Button('Go back to home', style={'backgroundColor':'white'}), href='/'),        
            ]),

                html.Div([dcc.Dropdown(id='dropdownlist2',
                                options = [{'label': s, 'value': s} for s in data_accelerometer.keys()],
                                value=['Accelerometer 1'],
                                multi=True),
                    ]),
                    html.Div(children=[html.Div(id='posxyz',
                    children=[
                                html.Div([daq.Gauge(
                                    id="x-gauge",
                                    label="X-axis",
                                    labelPosition="bottom",
                                    units="g",
                                    value=0,
                                    min=-8,
                                    max=8,
                                    showCurrentValue=True
                            ),], style={'display':'inline-block', 'paddingLeft':50, 'paddingRight':50}),
                        

                            html.Div([daq.Gauge(
                                id="y-gauge",
                                label="Y-axis",
                                labelPosition="bottom",
                                units="g",
                                value=0,
                                min=-8,
                                max=8,
                                showCurrentValue=True,
                            ),], style={'display':'inline-block', 'paddingLeft':50, 'paddingRight':50}),

                            html.Div([daq.Gauge(
                                id="z-gauge",
                                label="Z-axis",
                                labelPosition="bottom",
                                units="g",
                                value=0,
                                min=-8,
                                max=8,
                                showCurrentValue=True,
                            )], style={'display':'inline-block', 'paddingLeft':50, 'paddingRight':50})
                        ],
                        style={'text-align':'center'}
                    )
                ]
            )])


page_3_layout = html.Div(analog_tab())
page_4_layout = html.Div(digitalinput_tab())
page_5_layout = html.Div(digitaloutput_tab())
page_6_layout = html.Div(show_values_tab())
page_7_layout = html.Div(show_analog_tab())
