print("Hello,sherlock 221b")
from wifi_conn import do_connect
import Lcd_text as lt 
from ST7735 import TFT
import utime
import machine
print(utime.localtime())
from Iot_test import IOT_CONN
#from blinker_test import LED
do_connect()#wifi

tm = machine.Timer(-1)
tm.init(period=600000,mode=machine.Timer.PERIODIC,callback=lt.wd)

tm1 = machine.Timer(0)
tm1.init(period=1000,mode=machine.Timer.PERIODIC,callback=lt.currt_time)

iconn = IOT_CONN()
iconn.connect()

tm2 = machine.Timer(1)
tm2.init(period=120000,mode=machine.Timer.PERIODIC,callback=iconn.post_data)

#Á¬½Ówifi
#do_connect()

#³õÊ¼»¯blinker
lt.template()
#lt.write_text([30,20],"Hello ESP",1,TFT.BLUE)
while 1:
	lt.draw_smile()
	utime.sleep(5)
	lt.show_weather()
	utime.sleep(5)

#led=LED()
#led.run()