import dht
import machine


def get_temp_hum():
	d=dht.DHT22(machine.Pin(15))##使用15脚传输数据
	d.measure() #测量数据
	temperature=d.temperature()
	humidity=d.humidity()
	print("当前温度: %f   \n当前湿度: %f"%(temperature,humidity))
	return temperature,humidity