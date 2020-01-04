#import the adxl345 module
import time
import board
import busio
import adafruit_adxl34x


def accelerometer_values():
    i2c = busio.I2C(board.SCL, board.SDA)
    #create ADXL345 object
    accelerometer = adafruit_adxl34x.ADXL345(i2c)
    #print("Hi")
    while True:
        #print("Hi")
        return accelerometer.acceleration
        #print("%f %f %f"%accelerometer.acceleration)

#accelerometer_values()

