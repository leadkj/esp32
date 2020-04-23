#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import Pin

from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber
from Blinker.BlinkerDebug import *

auth = '7f185ddddb90'
ssid = '62-5-202'
pswd = 'anys888888'

BLINKER_DEBUG.debugAll()

Blinker.mode('BLINKER_WIFI')
Blinker.begin(auth, ssid, pswd)

button1 = BlinkerButton('btn-sps')
number1 = BlinkerNumber('num-abc')

counter = 0
pinValue = 0

p2 = Pin(2, Pin.OUT)
p2.value(pinValue)

def button1_callback(state):
    ''' '''

    BLINKER_LOG('get button state: ', state)

    button1.icon('icon_1')
    button1.color('#FFFFFF')
    button1.text('Your button name or describe')
    button1.print(state)

    global pinValue
    
    pinValue = 1 - pinValue
    p2.value(pinValue)

def data_callback(data):
    global counter
    
    BLINKER_LOG('Blinker readString: ', data)
    counter += 1
    number1.print(counter)

def heartbeat_callback():
    global counter
    
    button1.icon('icon_1')
    button1.color('#FFFFFF')
    button1.text('Your button name or describe')
    button1.print("on")

    number1.print(counter)

button1.attach(button1_callback)
Blinker.attachData(data_callback)
Blinker.attachHeartbeat(heartbeat_callback)

def run():
    while True:
        Blinker.run()
