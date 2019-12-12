n = int(input())

ost_a = [0]*3
ost_b = [0]*3
ost_c = [0]*3

ans = 0
t = list(map(int, input().split()))

for i in range(n):
    x = t[i]
    if i%3==0:
        ans += ost_a[(3-(x%3))%3]
        ost_a[x%3] += 1
    elif i%3==1:
        ans += ost_b[(3-(x%3))%3]
        ost_b[x%3] += 1
    else:
        ans += ost_c[(3-(x%3))%3]
        ost_c[x%3] += 1

print(ans)