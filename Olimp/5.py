def GCD(a,b):
    while b:
        a,b = b,a%b
    return a

n = int(input())
s = input()
a = []

for i in range(0,n):
    a.append(int(list(s.split(' '))[i]))

m = max(a)
d = []
for i in range(0,n):
    if a[i] != m:
        d.append(m-a[i])

z = d[0]
y = 0
for i in range(1,len(d)):
    z = GCD(z, d[i])

for i in range(0,len(d)):
    y += d[i]/z

print(int(y), z)