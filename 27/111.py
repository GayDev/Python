n = int(input())

buf = []
r = [0]*112
a,b = -1,-1
for _ in range(4):
    buf.append(int(input()))

for i in range(0,n-4):
    first = buf[i%4]
    k = first % 112
    r[k] = max(first,r[k])
    x = int(input())
    k = x % 112
    pair_k = (112-k) % 112

    if (r[k] + r[pair_k] > a + b) and (r[pair_k] > r[k]):
        a,b = r[pair_k],x

    buf[i%4] = x

if a+b == -2:
    print(-1)
else:
    print('%d\n%d %d' % (a+b, a, b))
    
