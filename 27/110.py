n = int(input())
a = []
i_mx = 0
x,y = 0,0

count = 0
for i in range(n):
    a.append(int(input()))
    if a[i] > a[i_mx]:
        i_mx = i

for i in range(i_mx):
    if a[i] % 3 == 0:
        x += 1

for i in range(i_mx+1, len(a)):
    if a[i] % 3 == 0:
        y += 1

print(x*(len(a)-i_mx-1) + y*(i_mx-x))

