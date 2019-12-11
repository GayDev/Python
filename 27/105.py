n = int(input())
buf = []
r = [0]*5
ans = 0
for _ in range(5):
    buf.append(int(input()))

for i in range(0,n-5):
    r[buf[i%5]%5] += 1

    x = int(input())
    ans += r[x%5]
    buf[i%5] = x

print('NO' if ans == 0 else ans)