#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:56:17 2019

@author: dust
"""

# Terminate message sent with EOL \n
import serial
import time

# Need to know which port teensy is connected to, baud rate
ser = serial.Serial(
        port = '/dev/ttyACM0', # Look for port
        baudrate = 9600,
        timeout = 0
        )

a = []
ticks = 0
i = 0

ser.flushInput()
ser.flushOutput()

while ser.in_waiting:
    ser.readline()

print("finished clearing")

while i < 10:
    print("start")
    ticks = 0
    i += 1
    a.clear()
    #while ser.readline():
    while ser.in_waiting:
        try:
            line = int(ser.readline().decode('utf-8').rstrip())
            ticks += 1
            a.append(line)
        except:
            print("IN EXCEPTION")
            continue
   # ser.flushInput()
   # ser.flushOutput()
        
        #time.sleep(.1)
    print("continuing")
    print("a: ")
    print(a)
    print("ticks: ")
    print(ticks)
    time.sleep(2)
        
ser.close()

print("done")
#print(a)

# print elapsed time
# Had interrupt function for reading from serial
# problem: might hit time limit won't be counting ticks during sleep