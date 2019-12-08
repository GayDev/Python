#How are duplicates removed from a given array in Java?

import random

a = []
for i in range(0,1000):
    a.append(int(random.random()*200))

#===============================================

b = {}
a1 = []

for i in range(0,1000):
    if not(a[i] in b):
        b[a[i]] = True
        a1.append(a[i])

print(a1)