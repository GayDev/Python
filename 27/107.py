n = int(input())

prev = 0
curr = 0
ans = 0

for i in range(n):
    x = int(input())
    if x == 0:
        prev += curr
        curr = 0
    else:
        curr += 1
        ans += prev
print(ans)