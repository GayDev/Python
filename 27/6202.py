m1,m2 = -1,-1
n = 0
t = int(input())
while t != 0:
    n += 1
    if t % 49 != 0:
        if t % 7 == 0:
            m1 = max(m1,t)
        else:
            m2 = max(m2,t)
    t = int(input())

exp = int(input())

if (m1 == -1) or (m2 == -1):
    c_n = 1
else:
    c_n = m1*m2

print('Введено чисел:', n)
print('Контрольное значение:', exp)
print('Вычисленное значение:', c_n)
if c_n == exp:
    print('Значения совпали')
else:
    print('Значения не совпали')