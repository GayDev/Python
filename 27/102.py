def sum(a):
    s = 0
    for i in a:
        s += i
    return s

n = int(input())
print()
buf = [0]*8
ans = 0
t = [-1]*8
for i in range(n):
    x = int(input())
    t[i%8] = x
    ans += sum(buf)-buf[(8-x)%8]
    buf[x%8] += 1
    if i >= 7:
        buf[t[(i+1)%8]%8] -= 1

print(ans)
