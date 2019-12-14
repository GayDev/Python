class node:
     def __init__(self,n,adj_1):
          self.n = n
          self.adj_1 = adj_1
          self.adj_2 = None
          self.adj_3 = None

n,m = map(int, input().split())

a = []

for _ in range(m):
     a.append(list(map(int, input().split())))

for i in range(m):
     beg = a[i][0]
     t = a[i][0]
     while True:
          for j in range(m):
               if j != i:
                    if a[j][0] == t:
                         t = a[j][1]
                    elif a[j][1] == t:
                         t = a[j][0]
    