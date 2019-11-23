import random

n = 100
a = []
for i in range(0,n):
    a.append(random.randint(1,1000000))

n = len(a)
ans = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans += a[i]*a[j]*a[k]
        #print('2!')
    print('1!')

print(ans%1000000007)