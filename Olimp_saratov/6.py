n = int(input())
mx = 0
mn = 3*n+1
for _ in range(n):
    x = list(map(int, input().split()))
    t = min(x)
    t2 = 3*n+1
    for i in x:
        if i < t2 and i > t:
            t2 = i
    
    mx = max(mx,t,t2)
    mn = min(mn,t,t2)

print(mx-mn)