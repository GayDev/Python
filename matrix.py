import random
import string
import time
import math
import os
from sty import fg,RgbFg
#--------------------------------------------------------------------------------
class color:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
    # def hsl_to_rgb(self,h,s,l):
        
#--------------------------------------------------------------------------------
class drop:
    def __init__(self,length,symbols_list):
        self.length=length
        self.symbols=[]
        self.symbols_list=symbols_list
        self.fill(length)
    
    def fill(self,length):
        for i in range(0,length):
            self.symbols.append(random.choice(self.symbols_list))
#--------------------------------------------------------------------------------
class column:
    def __init__(self,length):
        self.length=length
        self.is_busy=False
        self.new_drop=drop(2, ' ')
        self.symbols=[]
        for i in range(0,length):
            self.symbols.append(' ')

    def print(self):
        for i in range(0,self.length):
            print(self.symbols[i] + ' ',end='')
    
    def add_drop(self):
        if self.is_busy==True:
            return False
        else:
            self.new_drop=drop(random.randint(5,15),string.ascii_letters + string.punctuation)   #TODO
            self.is_busy=True
            return True
    
    def update(self):
        for i in range(len(self.symbols)-1):
            self.symbols[-1-i]=self.symbols[-2-i]
        self.symbols[0]=self.new_drop.symbols[-1]
        for i in range(len(self.new_drop.symbols)-1):
            self.new_drop.symbols[-1-i]=self.new_drop.symbols[-2-i]
            self.new_drop.symbols[0] = ' '
        if self.symbols[0]==' ':
            self.is_busy=False
#--------------------------------------------------------------------------------
class rain:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.columns=[]
        for i in range(0,self.width):
            self.columns.append(column(self.height))

        
    def update(self):
        for i in range(0,self.width):
            self.columns[i].update()
        

    def print(self,hilight_length,color_start,color_end):
        trail_colors = []
        for i in range(0,hilight_length):
            r = (color_end.r - color_start.r)/(hilight_length-1)*i + color_start.r
            g = (color_end.g - color_start.g)/(hilight_length-1)*i + color_start.g
            b = (color_end.b - color_start.b)/(hilight_length-1)*i + color_start.b
            trail_colors.append(color(int(r),int(g),int(b)))
        
        for i in range(0,self.height):
            for j in range(0,self.width):
                symbol = fg(0,230,0) + self.columns[j].symbols[i] + fg.rs
                print(symbol,end=' ')
            print('')
            
    def start(self,fps,gap,hilight_length,color_start,color_end):
        t = 0
        while 1==1:
            if t%gap == 0:
                self.columns[random.randint(0,self.width-1)].add_drop()
            self.update()
            os.system('clear')
            self.print(hilight_length,color_start,color_end)
            time.sleep(1/fps)
            t += 1
#--------------------------------------------------------------------------------
a = rain(55,60)
a.start(15,1,5,color(255,255,255),color(0,230,0))