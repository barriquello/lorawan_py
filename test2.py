#!/usr/bin/env python3
"""
    Test harness for dragino module - sends hello world out over LoRaWAN 5 times
"""
import logging
from time import sleep
import RPi.GPIO as GPIO
from dragino import Dragino

from remotedebugfeature import RemoteDebug

#remote_debug = True
#if remote_debug == True:
#    RemoteDebug() 

GPIO.setwarnings(False)

D = Dragino("dragino2.ini", logging_level=logging.DEBUG)
#D.join()
#while not D.registered():
#    print("Waiting")
#    sleep(2)
#sleep(10)
#for i in range(0, 5):
while 1:
    D.send("Hello World")
    print("Sent message")
    sleep(10)
