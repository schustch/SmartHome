#!/usr/bin/python

import smbus
import time
import RPi.GPIO as GPIO

#DEVICE_ADDRESS = 0x22 #=0x44
DEVICE_ADDRESS = 0x22

AMBIENT_LIGHT_SENSOR_ADDRESS = 0x4A
REG_CONF = 0x6
REG_DATA = 0x2

outputvalue = 0

I2C_BUS = 1

def readAmbienLightSensor():
    bus = smbus.SMBus(I2C_BUS)
    #inputvalue = bus.read_word_data(AMBIENT_LIGHT_SENSOR_ADDRESS,2)
    #bus.write_byte(AMBIENT_LIGHT_SENSOR_ADDRESS, 3)
    inputvalue = bus.read_i2c_block_data(AMBIENT_LIGHT_SENSOR_ADDRESS,10)     
    print "Val: " + str(inputvalue)

def initDevice():
    bus = smbus.SMBus(I2C_BUS) 
    bus.write_word_data(DEVICE_ADDRESS, REG_CONF, 0x0) 
    bus.write_word_data(0x21, 0x4, 0xffff)
    bus.write_word_data(0x21, 0x6, 0xffff)

def writeData(val):
    bus = smbus.SMBus(I2C_BUS) 
    bus.write_word_data(DEVICE_ADDRESS, REG_DATA, val)

def readData():
    bus = smbus.SMBus(I2C_BUS)
    inputvalue = bus.read_word_data(0x21,0)
    return inputvalue


#def enableOutput(val):

def Interrupt(channel):
   value = readData()
   processData(value)



def initInterrupt():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(18, GPIO.FALLING, callback = Interrupt, bouncetime = 10)

def writeOutput():
    global outputvalue
    writeData(outputvalue)

def processData(value):
    global outputvalue
    if value != 0:
        outputvalue = outputvalue ^ value
        writeOutput()

initDevice()
initInterrupt()
#while True:
#    readAmbienLightSensor()
#    time.sleep(1)


#readData()
#readData()
#readData()
#readData()




val = 0x1
while True:
    time.sleep(1)

for i in range(0, 25):
        writeData(inputvalue)
        #val = val<<1
        time.sleep(0.5) # delays for 5 seconds
        print inputvalue



#Write a single register
#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
#ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
#bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
