class elem:
    def __init__(self,v,n):
        self.v = v
        self.n = n

a = []
n = int(input())
for i in range(0,n):
    a.append(elem(int(input()),i))

a = a.sort()
print(a)