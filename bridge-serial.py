#!/usr/bin/env python3
"""
    Test harness for dragino module - sends hello world out over LoRaWAN 5 times
"""
import logging
from time import sleep
import RPi.GPIO as GPIO
from dragino import Dragino
import serial
from random import randrange

serialPortA = "/dev/ttyACM0"
serialPortU = "/dev/ttyUSB0"
baudRate = 115200

GPIO.setwarnings(False)

D = Dragino("dragino2.ini", logging_level=logging.ERROR)

ser = serial.Serial(serialPortA, baudRate, timeout=3)
ser.reset_input_buffer()
ser.reset_output_buffer()
timeout = 0
while 1:
    if D.state == 0:
        ans = b""
        while ser.in_waiting > 0:
            ans += ser.readline()
        if len(ans) == 0:
            ans = "?"
        D.set_mode(D.MODE.SLEEP)              
        print("Sent message:") 
        print(ans)
        ch = D.channels[randrange(len(D.channels))] #Pick a random channel        
        D.set_channel(ch)
        print ("@ch:{} @freq {} MHz".format(ch, D.freqs[D.channels.index(ch)]))
        D.set_dr(D.DR[2]) # set DR2
        D.send(ans)
    elif (D.state == 1 or D.state == 2):
        sleep(0.1)
        timeout += 1
        if timeout == 19: # 0,4s (max tx) + 1s (delay1) + 0,4s (max rx) + 0,1s (margin)
            print("rx 1 timeout")
            D.state = 2
            D.set_mode(D.MODE.STDBY)
            D.set_freq(D.dfreqs[0]) # goto rx win 2 / DR8
            D.set_dr(D.DR[8])
            D.set_mode(D.MODE.RXCONT)            
        if timeout == 30:
            print("rx 2 timeout")    
            timeout = 0
            D.state = 0
    else:
        sleep(10)
        timeout = 0
        D.state = 0         
       
