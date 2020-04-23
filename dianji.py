import time
from machine import Pin

speed = 2
STEPER_ROUND=512 #转动一圈(360度)的周期
ANGLE_PER_ROUND=STEPER_ROUND/360 #转动1度的周期
#print('ANGLE_PER_ROUND:',ANGLE_PER_ROUND)
p1 = Pin(19, Pin.OUT, value=0)
p2 = Pin(21, Pin.OUT, value=0)
p3 = Pin(22, Pin.OUT, value=0)
p4 = Pin(23, Pin.OUT, value=0)

def Front():
    global speed
       
    p1.value(1)
    p2.value(1)
    p3.value(0)
    p4.value(0)
    time.sleep_ms(speed)

    p1.value(0)
    p2.value(1)
    p3.value(1)
    p4.value(0)
    time.sleep_ms(speed)

    p1.value(0)
    p2.value(0)
    p3.value(1)
    p4.value(1)
    time.sleep_ms(speed)

    p1.value(1)
    p2.value(0)
    p3.value(0)
    p4.value(1)
    time.sleep_ms(speed)
     
def Back():
    global speed
     
    p1.value(1)
    p2.value(1)
    p3.value(0)
    p4.value(0)
    time.sleep_ms(speed)
     
    p1.value(1)
    p2.value(0)
    p3.value(0)
    p4.value(1)   
    time.sleep_ms(speed)
     
    p1.value(0)
    p2.value(0)
    p3.value(1)
    p4.value(1)
    time.sleep_ms(speed)
 
    p1.value(0)
    p2.value(1)
    p3.value(1)
    p4.value(0)
    time.sleep_ms(speed)
 
 
def Stop():
    p1.value(0)
    p2.value(0)
    p3.value(0)
    p4.value(0)
     
def Run(angle):
    global ANGLE_PER_ROUND
     
    val=ANGLE_PER_ROUND*abs(angle)
    if(angle>0):
        for i in range(0,val):
            Front()
    else:
        for i in range(0,val):
            Back()
    angle = 0
    Stop()
 
def main():
    Run(180)
    Run(-180)