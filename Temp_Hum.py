import dht
import machine
import utime

def get_temp_hum():
	p = machine.Pin(13)
	d=dht.DHT22(p)##使用14脚传输数据
	dht_stat = True
	while dht_stat:
		try:
			d.measure() #测量数据
			dht_stat = False
		except OSError as e:
			utime.sleep(3)
			dht_stat = True
			pass
	temperature=d.temperature()
	humidity=d.humidity()
	return temperature,humidity