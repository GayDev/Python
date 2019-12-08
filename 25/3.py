import random
import math

n = 100
a = []
for i in range(0,n):
    a.append(random.randint(0,1000))
km = 0
for i in range(0,n):
    k = 0
    for j in range(1,int(math.sqrt(a[i]))+1):
        if a[i] % j == 0:
            k += 1
    if k > km:
        km = k
        im = i
print(i+1, a[i])
