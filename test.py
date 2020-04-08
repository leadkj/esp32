from ST7735 import TFT
from machine import SPI,Pin
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18)
tft.initb2()
tft.rgb(True)

# Assign 2 pixels for fixed and invisible area
# (ST7735S frame buffer vertical size is 162 pixels)
tft.setvscroll(1, 1)

# Wrapper object for FBConsole
from ST7735fb import TFTfb
from petme128 import petme128
fb = TFTfb(tft, petme128)

# redirect MicroPython terminal to ST7735
from fbconsole import FBConsole
scr = FBConsole(fb, TFT.BLACK, TFT.WHITE)

import os
os.dupterm(scr) 