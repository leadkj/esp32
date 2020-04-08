from umqtt.simple import MQTTClient
import usocket as socket
import time
import wifi_conn

wifi.do_connect()

#设备证书信息
ProductKey = "a1jrk8qVkKr"
DeviceName = "orj3IBhW8BFNGR4FGEEA"
DeviceSecret = "w0gB4qUkcWmMFlXkDDWSOoDxCkbJHaH0"
timestamp=time.time()
#主要参数

#连接域名 server=<ProductKey>+".iot-as-mqtt.cn-shanghai.aliyuncs.com"
server=ProductKey+".iot-as-mqtt.cn-shanghai.aliyuncs.com"


#MQTT Connect报文参数

#1、mqttClinetId 
#mqttClientId = "<ClientId>"+"|securemode=3,signmethod=hmacsha1,timestamp=132323232|"

ClientId = "sher221b" #自定义
mqttClientId = "%s|securemode=3,signmethod=hmacsha1,timestamp=%d|"%(ClientId,timestamp)

#2、mqttUsername
#使用&拼接<DeviceName>和<ProductKey>

mqttUsername=DeviceName + "&" + ProductKey


#3、mqttPassword
"""
把以下参数按字典键名排序，再把键名都拼接起来（没有分隔符）生成content，
然后以DeviceSecret为盐，对content进行hma_sha1加密，最后二进制转为十六进制字符串表示

clientId
deviceName
productKey
timestamp

"""
data="".join(("clientId",ClientId,"deviceName",DeviceName,"productKey",ProductKey,"timestamp",str(timestamp)))


strBroker = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
Brokerport = 1883

user_name = "Demo_01&a1Mf4HZ5k**"  
user_password = "***************************************"

print("clientid:",ClientId,"\n","Broker:",strBroker,"\n","User Name:",user_name,"\n","Password:",user_password,"\n")


def connect():
	client = MQTTClient(client_id = ClientId,server= strBroker,port=Brokerport,user=user_name, password=user_password,keepalive=60) 
	#please make sure keepalive value is not 0
	
	client.connect()

	temperature =25.00
	while temperature < 30:
		temperature += 0.5		
	
		send_mseg = '{"params": {"IndoorTemperature": %s},"method": "thing.event.property.post"}' % (temperature)
		client.publish(topic="/sys/a1Mf4HZ5kET/Demo_01/thing/event/property/post", msg=send_mseg,qos=1, retain=False)
		
		time.sleep(3)

	while True:
		pass

	#client.disconnect()