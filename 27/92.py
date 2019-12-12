n = int(input())

buf = []
for i in range(6):
    buf.append(int(input()))

ans = 1001*1001
mn = [1001,1001]

for i in range(n-6):
    first = buf[i%6]
    if (first%2==0) and (mn[0]>=first):
        mn[0] = first
    elif (first%2 != 0) and (mn[1] >= first):
        mn[1] = first

    x = int(input())
    if x%2==0:
        ans = min(ans, x*mn[0], x*mn[1])
    else:
        ans = min(ans, x*mn[0])

    buf[i%6] = x

print(-1 if ans==1001*1001 else ans)
