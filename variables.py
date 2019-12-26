from collections import deque

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