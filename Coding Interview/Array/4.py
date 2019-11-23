#How do you find all pairs of an integer array whose sum is equal to a given number?

import random

a = []
for i in range(0,1000):
    a.append(int(random.random()*200))

#===============================================

class pair:
    def __init__(self,index1,index2):
        self.index1 = index1
        self.index2 = index2

pairs = []
n = int(input())

for i in range(0,1000):
    for j in range(i,1000):
        if a[i] + a[j] == n:
            pairs.append(pair(i,j))

print(a)

for i in range(0,len(pairs)):
    print(pairs[i].index1, ' ', pairs[i].index2, ' | ', a[pairs[i].index1], ' | ', a[pairs[i].index2])

