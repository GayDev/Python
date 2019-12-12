buf = []
ost = [0]*3

for i in range(5):
    buf.append(int(input()))

i = 0
ans = 0
while True:
    first = buf[i%5]
    ost[first%3] += 1

    x = int(input())
    if x==0:
        break
    ans += ost[(3-x%3)%3]
    buf[i%5] = x
    i+=1

print(ans)