import random

a = []
n = 30
for i in range(0,n):
    a.append(random.randint(0,10000))

j = 1000
for i in range(0,n):
    if (len(str(a[i]))==3) and (a[i]<j):
        j =a[i]

if j==1000:
    print('Nothing found!')
else:
    print(j)