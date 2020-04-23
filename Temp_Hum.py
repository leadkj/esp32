import dht
import machine

p=machine.Pin(14)

def get_temp_hum():
	d=dht.DHT22(p)##使用14脚传输数据
	d.measure() #测量数据
	temperature=d.temperature()
	humidity=d.humidity()
	print("当前温度: %f   \n当前湿度: %f"%(temperature,humidity))
	return temperature,humidity