from machine import Pin,PWM

from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber,BlinkerSlider
from Blinker.BlinkerDebug import *


auth = '7f185ddddb90'
ssid = '62-5-202'
pswd = 'anys888888'
p2 = Pin(2, Pin.OUT)
pwm=PWM(Pin(4,Pin.OUT))#led正极接3.3，负极接4号脚
pwm2=PWM(Pin(15,Pin.OUT))
class LED():

    def __init__(self):
        self.auth = auth
        self.ssid = ssid
        self.pswd = pswd

        BLINKER_DEBUG.debugAll()

        Blinker.mode('BLINKER_WIFI')
        Blinker.begin(auth, ssid, pswd)

        self.button1 = BlinkerButton('btn-sps')
        self.number1 = BlinkerNumber('num-abc')
        self.slider1 = BlinkerSlider("ran-jhb")
        self.slider2 = BlinkerSlider("ran-bqm")

        self.counter = 0
        self.pinValue = 0

        self.p2 = p2
        self.pwm = pwm
        self.pwm.freq(38000)
        self.pwm.duty(1)
        self.pwm2 = pwm2
        self.pwm2.freq(38000)
        self.pwm2.duty(1)
        self.p2.value(self.pinValue)
    def slider1_callback(self,value):
        
        value=1024-value
        self.pwm.duty(value)
        BLINKER_LOG('Slider read: ',value)
        
    def slider2_callback(self,value):
        
        self.pwm2.duty(value)
        BLINKER_LOG('Slider read: ',value)
    def button1_callback(self,state):

		    BLINKER_LOG('get button state: ', state)
        
		    self.pinValue=1-self.pinValue
		    if self.pinValue==1:
		    	self.button1.text('开')
		    else:
		    	self.button1.text('关')
		    self.p2.value(self.pinValue)
		    print(self.pinValue)

    def data_callback(self,data):

		    BLINKER_LOG('Blinker readString: ', data)
		    self.counter += 1
		    self.number1.print('counter',self.counter)

		
		

    def run(self):
    	  self.button1.attach(self.button1_callback)
    	  self.slider1.attach(self.slider1_callback)
    	  self.slider2.attach(self.slider2_callback)
    	  Blinker.attachData(self.data_callback)
    	  while True:
            try:
                Blinker.run()
            except OSError:
                pass

