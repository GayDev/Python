import math
n, m = map(int, input().split())   

mx = 0
below_max = 0
for i in range(n):
    x = int(input())
    if x > mx:
        below_max += (x-mx)*i
        mx = x
    else:
        below_max += mx-x

if m <= below_max:
    new_layers = 0
else:
    new_layers = math.ceil((m-below_max)/n)

print(mx+new_layers)