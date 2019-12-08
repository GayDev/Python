import random

N = 100
a = []
for i in range(0,N):
    a.append(random.randint(0,100))

x = int(input())
i = 0
j = 0
for i in range(0,N):
    if a[i] == x:
        print(i)
        j = 1
        break
if j == 0:
    print('Nothing found')
