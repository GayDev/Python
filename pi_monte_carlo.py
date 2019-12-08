import random
import math
real_pi = 3.1415926535897932384626433
in_circle=0
n=0
dp = 20
while True:
    n+=1
    x = random.random()
    y = random.random()
    if math.sqrt(x*x+y*y) < 1:
        in_circle += 1
    pi = 4*in_circle/n
    d = abs(pi-real_pi)
    if dp > d:
        print(n, ' : ', pi, ' : ', d)
        dp = d
