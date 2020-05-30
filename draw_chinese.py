def set_pixel(self, x, y, state):
    index = x + (int(y / 8) * self.columns)
    if state:
      self.buffer[self.offset + index] |= (1 << (y & 7))
     
    else:
      self.buffer[self.offset + index] &= ~(1 << (y & 7))
      
def draw_chinese(self,ch_str,x_axis,y_axis):
    offset_=0
    y_axis=y_axis*8#中文高度一行占8个
    x_axis=127-(x_axis*16)#中文宽度占16个
    for k in ch_str:
        code = 0x00#将中文转成16进制编码
        data_code = k.encode("utf-8")
        code |= data_code[0]<<16
        code |= data_code[1]<<8
        code |= data_code[2]
        byte_data=font.byte2[code]
        for y in range(0,16):
            a_=bin(byte_data[y]).replace('0b','')
            while len(a_)<8:
                a_='0'+a_
                
            b_=bin(byte_data[y+16]).replace('0b','')
            while len(b_)<8:
                b_='0'+b_
            for x in range(0,8):
                self.set_pixel(x_axis-x-offset_,y+y_axis,int(a_[x]))#文字的上半部分
                self.set_pixel(x_axis-x-8-offset_,y+y_axis,int(b_[x]))#文字的下半部分
        offset_+=16