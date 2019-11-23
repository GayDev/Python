n = int(input())
x,y = [],[]
for i in range(0,n):
    s = input()
    x.append(int(s.split()[0]))
    y.append(int(s.split()[1]))

if x[1]-x[0] == 0:
    x,y = y,x

k = (y[1]-y[0])/(x[1]-x[0])
b = y[0]-k*x[0]
t = -1
for i in range(2,n):
    if k*x[i] + b != y[i]:
        t = i
        break

if t!=-1:
    print('Yes')
    print('1 2', t+1)
else:
    print('No')
