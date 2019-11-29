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
        else:
            self.q = -1

a = []
n = int(input())
q = [0,0,0,0]
j = 0
for i in range(0,n):
    s = input()
    x,y = int(s.split()[0]),int(s.split()[1])
    if x != 0 and y != 0:
        a.append(point(x,y))
        q[a[j].q] += 1
        j += 1

n = len(a)
k = 0 
for i in range(0,4):
    if q[i] > k:
        k = i

print('K = %d' % (k+1))
print('M = %d' % q[k])

for i in range(0,n):
    if a[i].q == k:
        r = abs(a[i].x)
        break
for i in range(0,n):
    if a[i].q == k:
        r = min(r, abs(a[i].x), abs(a[i].y))
        ind = i

print('A = (%d, %d)' % (a[ind].x, a[ind].y))
print('R = %d' % r)