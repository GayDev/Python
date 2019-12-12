n = int(input())

mx1 = [-101,-101]
mx2 = [-101,-101]

for i in range(n):
    x = int(input())
    if x > mx1[x%2]:
        mx1[x%2]=x
    elif x > mx2[x%2]:
        mx2[x%2]=x

print(max(mx1[0]+mx2[0], mx1[1]+mx2[1]))