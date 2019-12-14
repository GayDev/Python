def path(v):
    if v==1:
        return [v]
    elif v%2==0:
        return [v]+path(int(v/2))
    else:
        return [v]+path(v-1)

n,k = map(int, input().split())

cnt = [0]*(n+1)

#for i in range(1,n+1):
    #x = path(i)
    #for j in x:
        #cnt[j]+=1
#ans = 1
#for i in range(1,len(cnt)):
    #if cnt[i] >= k:
        #ans = i

#print(ans)

from math import log
t = path(n)
print(log(n,2), end='\n\n\n\n')
for i in t:
    print(i)
