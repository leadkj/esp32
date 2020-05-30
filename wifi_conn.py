import network
import utime
import ntptime
import Lcd_text as lt

wifi_list = {
    "62-5-202":"anys888888",
    "LianLuo-Office":"LianLuo002280",
    "HONOR-20i":"picanoc1119"
}

def do_connect():
    lt.init_lcd()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    scan_list = wlan.scan()
    if not wlan.isconnected():
        print('connecting to network...')
        for ID in  scan_list:
            if ID[0].decode("utf-8") in wifi_list:
                wlan.connect(ID[0].decode("utf-8"),wifi_list[ID[0].decode("utf-8")])
                utime.sleep(3)
                break
        #wlan.connect('HONOR-20i', 'picanoc1119')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    ###同步时间
    ntptime.host='3.cn.pool.ntp.org'
    utime.sleep(5)
    time_ok = True
    while time_ok:
        try:
            ntptime.settime()
            time_ok = False
        except Exception as e:
            ntptime.settime()
            time_ok = True
            pass
        
