n = int(input())

ost3 = [0]*3
ost5 = [0]*3
t = list(map(int, input().split()))

for i in range(n):
    x = t[i]
    if x%5 == 0:
        ost5[x%3] += 1
    else:
        ost3[x%3] += 1

print(ost3)
print(ost5)

ans = ost5[0]*ost3[0] + \
      ost5[1]*ost3[2] + \
      ost5[2]*ost3[1] + \
      ost5[0]*(ost5[0]-1)//2 + \
      ost5[1]*ost5[2]

print(ans)