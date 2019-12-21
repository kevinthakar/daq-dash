import time

# Import the ADS1x15 module.
from flask import Flask, jsonify

# import Adafruit_ADS1x15


app = Flask(__name__)
i = 0


@app.route("/")
def getDetails():
    return "You Have connected to Machine "


# Create an ADS1115 ADC (16-bit) instance.
# adc = Adafruit_ADS1x15.ADS1115()
# adc = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

GAIN = 1


def getvalue():
    value1 = 10
    # value1=adc.read_adc(0,gain=GAIN)
    # value1=((value1/32768.0)*4.096*10) #Conversion value=>volatge=>current
    # value1=(21.875*value1-137.5) #Converting current to temperature through slope curve method
    temp = round(value1, 5)
    # print('Temperature in Celcius',value1)
    # print('\n')
    value2 = 20
    # value2=adc.read_adc(1,gain=GAIN)
    # value2=((value2/32768.0)*4.096*10)
    # value2=(3.1044*value2-12.088) #Converting current to vibration through slope curve method
    value2 = abs(value2)
    vibration = round(value2, 5)
    # print('Vibration in mm/s ',value2)
    # print('\n')
    value3 = 30
    # value3=adc.read_adc(2,gain=GAIN)
    # value3=((value3/32768.0)*4.096*10) #Converting value=>voltage=>current
    # value3=(0.18425*value3-0.7851)#Converting current to flow through slope curve method
    value3 = abs(value3)
    flow = round(value3, 5)
    # print('Flow in m/s ',value3)
    # print('\n')
    return temp, vibration, flow


@app.route('/currentdata')
def getCurrentMachineData():
    global i
    temp, vibration, flow = getvalue()
    machine_data = {
        "temp_value": temp,
        "flow_value": flow,
        "vibration_value": vibration,
        "unix": time.time()
        # time.sleep(0.5)
    }

    i = i + 1

    return jsonify(machine_data)


if __name__ == '__main__':
    app.run(debug=True)