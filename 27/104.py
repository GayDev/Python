n = int(input())
buf = []
r = [0]*3
ans = -1

for _ in range(5):
    buf.append(int(input()))

for i in range(n-5):
    first = buf[i%5]
    if (r[first%3] > first) or (r[first%3] == 0):
        r[first%3] = first

    x = int(input())
    if (abs(r[x%3] - x) > ans) and (r[x%3] != 0):
        ans = abs(r[x%3] - x)

    buf[i%5] = x

print('NO' if ans == -1 else ans)