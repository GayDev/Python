import os
os.system('clear')


n = int(input())
s = input()
a = []
x = 0
shots = 0
order = ''

for i in range(0,n):
    a.append(int(list(s.split(' '))[i]))

while True:
    if max(a) != 0:
        i = a.index(max(a))
        shots += a[i]*x + 1
        order += str(i+1) + ' '
        x+= 1
        a[i] = 0
    else:
        break

print(shots)
print(order)

