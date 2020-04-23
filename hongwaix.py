import time
from machine import Pin

p13 = Pin(13,Pin.IN)
p2 = Pin(2,Pin.OUT)
def get_value():
    value = p13.value()
    if value == 1:
        print("����")
    return value
    
    
def led_on():
    while 1:
        value=get_value()
        p2.value(value)
        if value == 1:
            time.sleep(10)
        else:
            time.sleep(1)