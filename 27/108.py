n = int(input())
k = 3           #mod base
prev = [0]*k
curr = [0]*k
t = 0
while True:
    t += 1
    x = int(input())
    if x==0:
        break
    prev[x%k] += 1

ans = 0
for i in range(n-t):
    x = int(input())
    if x == 0:
        for i in range(k):
            prev[i] += curr[i]
        curr = [0]*k
    else:
        t = x%k
        curr[t] += 1 
        pair_t = (k-t)%k
        ans += prev[pair_t]

print(ans)