print("Hello,sherlock 221b")
from wifi_conn import do_connect
from blinker_test import LED

#����wifi
do_connect()

#��ʼ��blinker

led=LED()
led.run()