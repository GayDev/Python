import random

k = 7
even = [0]*k
odd = [0]*k
n = int(input())
ans = 0
for i in range(n):
    x = int(input())

    for j in range(0, k-1):
        for l in range(j+1, k):
            if ((x%k + j + l) % 7 == 0) and (x%2==0):
                ans += even[j]*odd[l]
                ans += even[l]*odd[j]
            elif ((x%k + j + l) % 7 == 0) and (x%2==1):
                ans += odd[j]*odd[l]
                ans += even[j]*even[l]
    
    if x%2==0:
        even[x%k] += 1
    else:
        odd[x%k] += 1

print(ans)