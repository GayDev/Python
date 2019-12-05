n = int(input())
fm = [-1]*144
a, b = [-1,-1], [-1,-1]
for i in range(n):
    t = int(input())
    if ((t%144 == 72) and (t < a[0])) or (a[0] == -1):
        a[1] = a[0]
        a[0] = t
    elif ((t%144 == 0) and (t < b[0])) or (b[0] == -1):
        b[1] = a[0]
        b[0] = t
    elif fm[t%144] > t or fm[t%144] == -1:
        fm[t%144] = t

ans = a
for i in range(1,72):
    i


