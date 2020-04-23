from umqtt.simple import MQTTClient
import usocket as socket
import time
import dht
import machine
import wifi_conn as wifi

wifi.do_connect()
d=dht.DHT22(machine.Pin(13))

#设备证书信息
ProductKey = "a110jrdi9yy"
DeviceName = "My_ESP"
DeviceSecret = "ub5iU9VokB4FPAeXePrrTfNGKsn08mQ8"
timestamp=789  #自定义
#主要参数

#连接域名 server=<ProductKey>+".iot-as-mqtt.cn-shanghai.aliyuncs.com"
mttq_Server=ProductKey+".iot-as-mqtt.cn-shanghai.aliyuncs.com"
mttq_Port = 1883

#MQTT Connect报文参数

#1、mqttClinetId 
#mqttClientId = "<ClientId>"+"|securemode=3,signmethod=hmacsha1,timestamp=132323232|"

ClientId = "My_ESP" #自定义
mqtt_ClientId = "%s|securemode=3,signmethod=hmacsha1,timestamp=%d|"%(ClientId,timestamp)

#2、mqttUsername
#使用&拼接<DeviceName>和<ProductKey>

mqtt_Username=DeviceName + "&" + ProductKey


#3、mqttPassword
"""
把以下参数按字典键名排序，再把键名都拼接起来（没有分隔符）生成content，
然后以DeviceSecret为盐，对content进行hma_sha1加密，最后二进制转为十六进制字符串表示

clientId
deviceName
productKey
timestamp
可以用生成器生成密码，因为这里的信息都是可以不变的
"""

mttq_Password = "80C75DE5D8A68B0FBE78B35C68B1A3EF7C86A6C1"



def connect():
	client = MQTTClient(client_id = mqtt_ClientId,server= mttq_Server,port=mttq_Port,user=mqtt_Username, password=mttq_Password,keepalive=60) 
	#please make sure keepalive value is not 0
	
	client.connect()
	temperature=0
	while temperature < 30:
				
		d.measure()
		temperature=d.temperature()
		humidity = d.humidity()
		#send_mseg = '{"CurrentTemperature":%s}' % (temperature)
		send_mseg = '{"params": {"CurrentTemperature": %s,"CurrentHumidity": %s},"method": "thing.event.property.post"}' % (temperature,humidity)
		client.publish(topic="/sys/a110jrdi9yy/My_ESP/thing/event/property/post", msg=send_mseg,qos=1, retain=False)
		time.sleep(10)
	while True:
		pass

	#client.disconnect()