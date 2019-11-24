class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if x>0 and y>0:
            self.q = 0
        elif x<0 and y>0:
            self.q = 1
        elif x<0 and y<0:
            self.q = 2
        elif x>0 and y<0:
            self.q = 3

n = int(input())
a = []
q = [0,0,0,0]
j = 0
for i in range(0,n):
    inp = input()
    x = int(inp.split(' ')[0])
    y = int(inp.split(' ')[1])
    if x!=0 and y!=0:
        a.append(point(x,y))
        q[a[j].q] += 1
        j += 1

K = q.index(max(q))+1

M = 0
n = j
A = 1000
for i in range(0,n):
    if a[i].q == K-1:
        M += 1
        if a[i].x ** 2 + a[i].y ** 2 < A:
            x = a[i].x
            y = a[i].y
        

print('K =', K)
print('M =', M)
print('A = (', x, ';', y, ')')
print('R =', min(abs(x), abs(y)))