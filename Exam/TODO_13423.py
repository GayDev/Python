def sum(a):
    if a < 10:
        return a
    else:
        return a % 10 + sum(a // 10)

n = int(input())
a = {}

for _ in range(0,n):
    ip = int(input())
    if sum(ip) in a:
        a[sum(ip)] += 1
    else:
        a[sum(ip)] = 1
m = a[a.keys()[0]]
for i in a.keys():
    if a[i] > m:
        m = i
    elif (a[i] == a[m]) and (i < m):
        m = i


print(a)
