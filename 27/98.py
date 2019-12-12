n = int(input())

mn = [100001,100001]
count = [0,0]
for i in range(n):
    x = int(input())
    if x < mn[0]:
        mn[1] = mn[0]
        mn[0] = x
        count[1] = count[0]
        count[0] = 1
    elif x==mn[0]:
        count[0] += 1
    elif x < mn[1]:
        mn[1] = x
        count[1] = 1
    elif x==mn[1]:
        count[1] += 1
t = 0
if mn[0]==mn[1]:
    n = count[0]+count[1]
    ans = int(n + (n>3)*n*(n-3)/2)
    t = mn[0]*2
elif count[0] > 1:
    n = count[0]
    ans = int(n + (n>3)*n*(n-3)/2)
    t = mn[0]*2
else:
    ans = count[1]
    t = mn[0]+mn[1]

print(mn)
print(count)
print(t,ans)
