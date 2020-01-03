import dash
import dash_core_components as dcc
import dash_html_components as html
import time
import dash_daq as daq
from collections import deque
import plotly.graph_objs as go
import random
import plotly.graph_objects as go

from thermocouple import temp_data
from variables import *
from components_layout import *



def update_thermocouple_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8):

        i = 0
        while i<=10:
            times.append(time.time())
            l = temp_data()
            print(l)
    #if len(times) == 1:
    #starting relevant values
            thermocouple_1.append(l[0])
            thermocouple_2.append(l[1])
            thermocouple_3.append(l[2])
            thermocouple_4.append(l[3])
            thermocouple_5.append(l[4])
            thermocouple_6.append(l[5])
            thermocouple_7.append(l[6])
            thermocouple_8.append(l[7])
            i = i+1
        
        return times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8

times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8 = update_thermocouple_values(times, thermocouple_1, thermocouple_2, thermocouple_3, thermocouple_4, thermocouple_5, thermocouple_6, thermocouple_7, thermocouple_8)