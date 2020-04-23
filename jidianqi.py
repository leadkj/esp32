##继电器esp32,手上的2路继电器为常闭开关

import machine

p5=machine.Pin(5,machine.Pin.OUT) #OUT为常开状态COM和NO接线柱为链接状态
#p5=machine.Pin(5,machine.Pin.IN)  #IN为常闭状态COM和NC接线柱为连接状态