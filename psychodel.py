from sty import fg, RgbFg
import colorsys
import time

def snake(a, sym):
    while True:
        for i in range(0,a):
            s = fg(255,150,150) + sym + fg.rs
            print(s, end='')
        print('\n' + ' '*(a-1))
        

snake(6,'#')