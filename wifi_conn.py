import network
import utime
import ntptime
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('LianLuo-Office', 'LianLuo002280')
        #wlan.connect('62-5-202', 'ayns888888')
        #wlan.connect('HONOR-20i', 'picanoc1119')
        while not wlan.isconnected():
            utime.sleep(1)
    print('network config:', wlan.ifconfig())
    ###同步时间
    ntptime.settime()
