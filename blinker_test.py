from machine import Pin,PWM
import threading,time
from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber,BlinkerSlider
from Blinker.BlinkerDebug import *
from dianji import Run
from hongwaix import get_value
from Temp_Hum import get_temp_hum
import ntptime
ntptime.host='s1a.time.edu.cn' #北京邮电大学ntp服务器


auth = '7f185ddddb90'
ssid = '62-5-202'
pswd = 'anys888888'
p2 = Pin(2, Pin.OUT)
p5 = Pin(5,Pin.OUT)  #继电器
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

        self.button1 = BlinkerButton('btn-of9')
        self.button2 = BlinkerButton('btn-a1x')#开窗帘
        self.button3 = BlinkerButton('btn-qni')#关窗帘
        self.button4 = BlinkerButton('btn-5gx')#1号继电器
        self.number1 = BlinkerNumber('num-abc')
        self.number2 = BlinkerNumber('num-kf5')#发送温度
        self.number3 = BlinkerNumber('num-50b')#发送湿度
        self.slider1 = BlinkerSlider("ran-jhb")
        self.slider2 = BlinkerSlider("ran-bqm")

        self.counter = 0
        self.pinValue = 0
        

        self.p2 = p2
        self.p5 = p5
        self.value5 = 0
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
    def button2_callback(self,state):
        t=threading.Thread(target=Run,args=(720,))
        t.start()
    def button3_callback(self,state):
        t=threading.Thread(target=Run,args=(-720,))
        t.start()
		
		
		#继电器
    def button4_callback(self,state):
        self.value5 = 1-self.value5
        self.p5.value(self.value5)
        print(self.value5)
    def data_callback(self,data):

		    BLINKER_LOG('Blinker readString: ', data)
		    self.counter += 1
		    self.number1.print(self.counter)

        
    def heartbeat_callback(self):
        t,h = get_temp_hum()
        self.number2.print(t)
        self.number3.print(h)
		
		

    def run(self):
    	  self.button1.attach(self.button1_callback)
    	  Blinker.attachData(self.data_callback)
    	  Blinker.attachHeartbeat(self.heartbeat_callback)
    	  self.button2.attach(self.button2_callback)
    	  self.button3.attach(self.button3_callback)
    	  self.button4.attach(self.button4_callback)
    	  self.slider1.attach(self.slider1_callback)
    	  self.slider2.attach(self.slider2_callback)

    	  while True:
            value=get_value()
            try:
                Blinker.run()
            except OSError:
                pass

