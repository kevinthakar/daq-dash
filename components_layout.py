#!/home/pi/MyDAQApp/daq/bin/python3

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
#import RPi.GPIO as GPIO
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

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(5, GPIO.IN)
#GPIO.setup(6, GPIO.IN)
#GPIO.setup(13, GPIO.IN)
#GPIO.setup(19, GPIO.IN)
#GPIO.setup(26, GPIO.IN)
#GPIO.setup(16, GPIO.IN)
#GPIO.setup(20, GPIO.IN)
#GPIO.setup(21, GPIO.IN)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(17, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)

#v1=GPIO.input(5)
#v2=GPIO.input(6)
#v3=GPIO.input(13)
#v4=GPIO.input(19)
#v5=GPIO.input(26)
#v6=GPIO.input(16)
#v7=GPIO.input(20)
#v8=GPIO.input(21)

#print(v1,v2)



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





   

app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])

a = 0

index_page = html.Div(children=[

    html.Div([html.Div([html.H3('Welcome to Portable C-DAQ!')], style={'text-align':'center'}),
    html.Br(),
    html.Div([html.Img(src='assets/image2vector (1).svg', style={'width':'15%'})], style={'text-align':'center'}),
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



page_2_layout = html.Div([accelerometer_layout()])
page_3_layout = html.Div(analog_tab())
page_4_layout = html.Div(digitalinput_tab())
page_5_layout = html.Div(digitaloutput_tab())
page_6_layout = html.Div(show_values_tab())
page_7_layout = html.Div(show_analog_tab())
