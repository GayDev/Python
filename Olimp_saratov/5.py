n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    
    for j in range(m-1):
        if x[j+1]==1:
            x[j]=2
        elif x[j]==1:
            x[j+1]=2
    
    a.append(x)
    
for i in range(n-1):
    for j in range(m):
        if a[i+1][j]==1:
            a[i][j]=2
        elif a[i][j]==1:
            a[i+1][j]=2

t = []
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            t.append([i,j])

ans = 0
for i in range(len(t)-1):
    for j in range(i+1,len(t)):
        dx = abs(t[i][0] - t[j][0])
        dy = abs(t[i][1] - t[j][1])
        if dx+dy != 1:
            ans+=1
        
print(ans)