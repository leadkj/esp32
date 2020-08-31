from umqtt.simple import MQTTClient
import usocket as socket
import time
from Temp_Hum import get_temp_hum
import machine


#设备证书信息
ProductKey = "xxxxxxx"
DeviceName = "My_ESP"
DeviceSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
timestamp=789  #自定义
#主要参数

class IOT_CONN():

	def __init__(self):
		self.ProductKey = ProductKey
		self.DeviceName = DeviceName
		self.DeviceSecret = DeviceSecret
		self.timestamp = 789
		#连接域名 server=<ProductKey>+".iot-as-mqtt.cn-shanghai.aliyuncs.com"
		self.mttq_Server=ProductKey+".iot-as-mqtt.cn-shanghai.aliyuncs.com"
		self.mttq_Port = 1883
		#MQTT Connect报文参数

		#1、mqttClinetId 
		#mqttClientId = "<ClientId>"+"|securemode=3,signmethod=hmacsha1,timestamp=132323232|"

		self.ClientId = "My_ESP" #自定义
		self.mqtt_ClientId = "%s|securemode=3,signmethod=hmacsha1,timestamp=%d|"%(self.ClientId,self.timestamp)

		#2、mqttUsername
		#使用&拼接<DeviceName>和<ProductKey>

		self.mqtt_Username=self.DeviceName + "&" + self.ProductKey


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

		self.mttq_Password = "80C75DE5D8A68B0FBE78B35C68B1A3EF7C86A6C1"
		self.client = None


	def connect(self):
		self.client = MQTTClient(client_id = self.mqtt_ClientId,server= self.mttq_Server,port=self.mttq_Port,user=self.mqtt_Username, password=self.mttq_Password,keepalive=3600) 
		#please make sure keepalive value is not 0
		res = self.client.connect()
		if not res:
			print("device connect success")
		else:
			print("device connect faild")






	def post_data(self,callback):#callback用于Timer定时器回调
		temperature ,humidity = get_temp_hum()
		#send_mseg = '{"CurrentTemperature":%s}' % (temperature)
		send_mseg = '{"params": {"CurrentTemperature": %s,"CurrentHumidity": %s},"method": "thing.event.property.post"}' % (temperature,humidity)
		if self.client:
			try:
				self.client.publish(topic="/sys/a110jrdi9yy/My_ESP/thing/event/property/post", msg=send_mseg,qos=1, retain=False)
			#time.sleep(30)
			except Exception as e:
				print(e)
				self.connect()
				self.client.publish(topic="/sys/a110jrdi9yy/My_ESP/thing/event/property/post", msg=send_mseg,qos=1, retain=False)

			# while True:
			# 	pass
	def disconnect(self):
		if self.client:
		    self.client.disconnect()
