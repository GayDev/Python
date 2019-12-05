n = int(input())
even = []
odd = []
for i in range(0,n):
    s = int(input())
    if s % 2 == 0:
        even.append(s)
    else:
        odd.append(s)
d = int(input())

r = max(even) + max(odd)
if r % 2 == 0:
    r = -1
print('Вычисленное контрольное значение: %d' % r)
if r==d:
    print('Контроль пройден')
else:
    print('Контроль не пройден')