n = int(input()) #8 75 123 5 40 15 3 65 80 ++++ 3 123
mn = [10001]*60
mx = [0]*60

a = mx[0]
b = mn[0]

for i in range(0,n):
    t = int(input())
    if mn[t%60] > t:
        mn[t%60] = t
    if mx[t%60] < t:
        mx[t%60] = t
t = abs(mx[0]-mn[0])

for i in range(0,60):
    if abs(mx[i]-mn[i]) > t and mn[i] != 10001 and mx[i] != 0:
        t = abs(mx[i]-mn[i])
        a = mx[i]
        b = mn[i]

print(a,b)