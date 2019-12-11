n = int(input())    # 0 -> 3 6 9 ...
                    # 1 -> 2 5 8 ...
                    # 2 -> 1 4 7 ...

t = list(map(int, input().split()))
buf = []
ost_a, ost_b, ost_c = [0]*3,[0]*3,[0]*3

for i in range(1,n+1):
    x = t[i-1]
    if (i%3==0):
        if (x % 3 == 0) and (ost_a[0] <= x):
            a = ost_a[0]
            ost_a[0] = x
        else:
            ost_a[x%3] = max(ost_a[x%3], x)
    elif (i%3==1):
        ost_b[x%3] = max(ost_b[x%3], x)
    else:
        ost_c[x%3] = max(ost_c[x%3], x)

ans = 0

ans = max(ans, a+ost_a[0])
ans = max(ans, ost_a[1]+ost_a[2])
ans = max(ans, ost_b[0]+ost_c[0])
ans = max(ans, ost_b[1]+ost_c[2])
ans = max(ans, ost_c[1]+ost_b[2])

print(-1 if ans == 0 else ans)
