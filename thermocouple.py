import serial
#from flask import Flask

def temp_data():
    ser = serial.Serial('/dev/ttyACM0',9600)
    values = []
    temp_list =[]
    while True:
        data = ser.readline()   #read data from serial
        if data:                #if there is data, append it to s
            values.append(data)
        if len(values) == 8:         #when s is 3 elements long, (all data has been retrieved)
            #print(s)
            for temperature in values:
                temperature = temperature.decode("utf-8")
                if (temperature!='NaN'):
                    temperature = temperature.rstrip('\r\n')
                    temp_list.append(temperature)
                else:
                    temp_list.append(123)
            return temp_list