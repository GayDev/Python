n = int(input())
a = []
buf = []
ost = [0]*8

for i in range(4):
    buf.append(int(input()))

count = 0
for i in range(n-4):
    first = buf[i%4]
    k = first % 8
    ost[k] += 1
    x = int(input())
    k = x % 8
    dk = (8 - k) % 8
    count += ost[dk]
    buf[i%4] = x

print(count)
