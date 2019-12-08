def binary_search(a,s,e,f):
    index = int((e+s)/2)
    if e-s==1 or e-s==0:
        return index
    elif f>a[index]:
        return binary_search(a,index,e,f)
    elif f<a[index]:
        return binary_search(a,s,index,f)
    else:
        return index-1

import random

b = []
t = []
q = []

n = 1000000
b.append(0)
t.append(23)
for i in range(1,n):
    b.append(b[i-1]+random.randint(1,1000))
    t.append(t[i-1]+random.randint(1,100))
print('DONE')
m = 1000000
for i in range(0,m):
    q.append(random.randint(1,100000000))

print('DONE')
for i in range(0,m):
    if q[i] > b[n-1]:
        print(t[n-1]*q[i])
    else:
        print(t[binary_search(b,0,n-1,q[i])]*q[i])