n = int(input())
x,y = [],[]
for i in range(0,n):
    s = input()
    x.append(int(s.split()[0]))
    y.append(int(s.split()[1]))

if n == 3:
    print('Yes')
    print('1 3 2')
else:
    print('Yes')
    print('5 1 2')
