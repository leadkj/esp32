import ntptime
import time
ntptime.host='s1a.time.edu.cn'

a=1
while a:
    try:
        print('sync time')
        ntptime.settime()
        print("sync time ok")
        time.sleep(500)
    except Exception as e:
        print("sync time faild")
        time.sleep(3)
        