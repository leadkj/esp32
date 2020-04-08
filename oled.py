from machine import Pin ,I2C



class OLED(I2C):
	def __init__(self,scl=Pin(0),sda=Pin(4),freq=200000):
		super().__init__(-1,scl,sda)
		self.i2c_address= 60
		init_command=[
			0xae,
			0x00,0x10,
			0xd5,0x80,
			0xa8,0x3f,
			0xd3,0x00,
			0xB0,
			0x40,
			0x8d,0x14,
			0xa1,
			0xc8,
			0xda,0x12,
			0x81,0xff,
			0xd9,0xf1,
			0xdb,0x30,
			0x20,0x02,
			0xa4,
			0xa6,
			0xaf]
		self.writeto_mem(self.i2c_address,0x00,bytes([0xae]))
		self.writeto_mem(self.i2c_address,0x00,bytes([0x8d]))
		self.writeto_mem(self.i2c_address,0x00,bytes([0x10]))
		self.Clear()
		for i in init_command:
			self.writeto_mem(self.i2c_address,0x00,bytes([i]))

	def Clear(self):
		for i in range(8):
			self.writeto_mem(self.i2c_address,0x00,bytes([0xb0+i]))
			self.writeto_mem(self.i2c_address,0x00,bytes([0x10]))
			self.writeto_mem(self.i2c_address,0x00,bytes([0x00]))
			for n in range(128):
				self.writeto_mem(self.i2c_address,0x40,b'\x00')
