#import the adxl345 module
import time
import board
import busio
import adafruit_adxl34x


def accelerometer_values():
    i2c = busio.I2C(board.SCL, board.SDA)
    #create ADXL345 object
    # accelerometer = adafruit_adxl34x.ADXL345(i2c) 
    while True:
        time.sleep(1)
        return accelerometer.acceleration
        #print("%f %f %f"%accelerometer.acceleration)

