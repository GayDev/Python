#How do you find duplicate numbers in an array if it contains multiple duplicates?

import random

a = []
for i in range(0,int(input())):
    a.append(int(input()))

#===============================================

duplicates = {}
b = {}

for i in range(0,len(a)):
    if a[i] in b:
        duplicates[a[i]] = True
    else:
        b[a[i]] = True

print(duplicates.keys())

