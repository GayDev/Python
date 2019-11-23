n = int(input())
s = input().split()
a = []
sm = 0
for i in range(0,n):
    if int(s[i])!=0:
        a.append(int(s[i]))
        sm += int(s[i])
n = len(a)
ans = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans += a[i]*a[j]*a[k]

print(ans)