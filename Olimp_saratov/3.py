n = int(input())
k = int(input())

buf = []
s = 0

for i in range(k):
    x = int(input())
    buf.append(x)
    s += x
    
sm = s
mn=s

for i in range(n-k):
    first = buf[i%k]
    mn = min(sm,mn)
    x = int(input())
    sm -= first
    sm += x
    s += x
    
print(s+2*(0-mn))