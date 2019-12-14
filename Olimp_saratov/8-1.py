n,k = map(int, input().split())

cnt = [0]*(n+1)
num = [i for i in range(1,n+1)]
beg = num[:]
find=False
ans = 1
while True:
    for i in range(n):
        t = num[i]
        if t==1:
            cnt[1]+=1
        elif t%2==0:
            cnt[t]+=1
            t //= 2
            num[i] = t
        else:
            cnt[t]+=1
            t -= 1
            num[i] = t
    
    if find:
        break

print(ans)