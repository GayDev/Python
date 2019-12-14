from math import log as ln
from math import cos 
from math import sin
from math import pi

f = open('input.txt', 'r')
n,r,k = map(int, f.read().split())

s = r*r*n*sin(2*pi/n)/2
s = ln(s) + 2*k*ln(cos(pi/n))

f.close()
f = open('output.txt', 'w')
f.write(str(s))
f.close()