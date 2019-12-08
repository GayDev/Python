#How do you find the duplicate number on a given integer array?

import random

a = []
for i in range(0,1000):
    a.append(i)
for i in range(0,450):
    index1 = int(random.random()*1000)
    index2 = int(random.random()*1000)
    t = a[index1]
    a[index1] = a[index2]
    a[index2] = t

a.append(a[index1])
print(a[index1])
#===============================================

b = {}

for i in range(0,1001):
    if a[i] in b:
        print(a[i], ' is a duplicate number.')
    else:
        b[a[i]] = True