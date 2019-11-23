a = []
n = 5
for i in range(0,n):
    a.append(int(input()))

im = 0
km = 1
for i in range(0,n):
    k = 1
    for j in range(1,a[i]):   #Считаем делители
        if a[i] % j == 0:
            k += 1
    print('%d: %d' % (a[i], k))
    if k > km:
        km = k
        im = i

print(im+1)