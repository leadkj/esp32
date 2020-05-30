from ST7735 import TFT,TFTColor
from machine import SPI,Pin
from petme128 import petme128
import threading
import utime
import machine
from Temp_Hum import get_temp_hum
weather_data = get_temp_hum()

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(19), mosi=Pin(18), miso=Pin(21))
tft=TFT(spi,5,4,2)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)





def currt_time(callback):
	
	t = ["0"+str(i) if len(str(i))<2 else str(i) for i in utime.localtime()]
	time = "%s:%s:%s"%("0"+str(int(t[3])+8) if len(str(int(t[3])+8))<2 else str(int(t[3])+8) ,t[4],t[5])
	tft.text(aPos=[70,12],aString=time,aFont=petme128,aColor=TFT.BLUE,aSize=0.8)

def template():
	tft.text(aPos=[12,3],aString='ESP32',aFont=petme128,aColor=TFT.WHITE,aSize=1.2)
	tft.line([1,23],[128,23],TFT.WHITE)
	tft.line([1,110],[128,110],TFT.WHITE)
	tft.text(aPos=[25,115],aString='@ weijx.top',aFont=petme128,aColor=TFT.WHITE,aSize=0.8)
	
	#t = threading.Thread(target=currt_time)
	#t.start()
def clear_data_zone(aColor=TFT.BLACK):
	tft.fillrect((0, 24), (128,86), aColor)

def init_lcd():
	write_text((10,30),"Initing....",1,TFT.WHITE)

def write_text(aPos,aString,aSize,aColor):#((30,2),"Hello ESP",1,TFT.BLUE)
	aPos = (aPos[0],aPos[1]+24)
	tft.text(aPos=aPos,aString=aString,aFont=petme128,aColor=aColor,aSize=aSize)

def draw_smile():
	tft.fillrect((0, 24), (128,86), TFT.BLACK)
	write_text((30,2),"Hello ESP",1,TFT.BLUE)
	tft.fillcircle((65,75),30,TFT.WHITE)
	tft.fillcircle((50,65),10,TFT.BLACK)
	tft.fillcircle((80,65),10,TFT.BLACK)
	tft.fillcircle((50,65),4,TFT.WHITE)
	tft.fillcircle((80,65),4,TFT.WHITE)
	tft.fillrect((60, 90), (10,3), TFT.BLACK)
	

def wd(t):
	global weather_data
	weather_data = get_temp_hum()

def show_weather():
	tft.fillrect((0, 24), (128,86), TFT.BLACK)
	global weather_data
	write_text((2,10),"TEMP: %d" %int(weather_data[0]),1.2,TFT.WHITE)
	write_text((2,30),"HUMI: %d" %int(weather_data[1]),1.2,TFT.WHITE)


def show_img(f):
	tft.fill(TFT.BLACK)
	if f.read(2) == b'BM':  #header
		dummy = f.read(8) #file size(4), creator bytes(4)
		offset = int.from_bytes(f.read(4), 'little')
        hdrsize = int.from_bytes(f.read(4), 'little')
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
            depth = int.from_bytes(f.read(2), 'little')
            if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                print("Image size:", width, "x", height)
                rowsize = (width * 3 + 3) & ~3
                if height < 0:
                    height = -height
                    flip = False
                else:
                    flip = True
                w, h = width, height
                if w > 128: w = 128
                if h > 160: h = 160
                tft._setwindowloc((0,0),(w - 1,h - 1))
                for row in range(h):
                    if flip:
                        pos = offset + (height - 1 - row) * rowsize
                    else:
                        pos = offset + row * rowsize
                    if f.tell() != pos:
                        dummy = f.seek(pos)
                    for col in range(w):
                        bgr = f.read(3)
                        tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))