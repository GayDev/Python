q = int(input())
a = []

for i in range(0,q):
    a.append(int(input())-1)

for i in range(0,q):
    index = 0
    n = 1
    j = 1
    while index < a[i]:
        index += len(str(n))
        if n != j:
            n+=1
        else:
            j += 1
            n = 1
    if index == a[i]:
        ans = str(n)[0]
    else:
        ans = str(n-1)[-(index - a[i])]
    print(ans)

