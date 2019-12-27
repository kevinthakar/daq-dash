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