n,sx,sy = map(int, input().split())

q1,q2,q3,q4 = 0,0,0,0
m1 = [10**9+1, 0]
m2 = [10**9+1, 0]
m3 = [0, 0]
m4 = [0, 0]
c1 = [10**9+1, 10**9+1]
c2 = [0, 10**9+1]
c3 = [0, 0]
c4 = [10**9+1, 0]

for i in range(n):
    x = list(map(int, input().split()))
    if x[0]>sx and x[1] > sy:
        c1[0] = min(c1[0], x[0])
        c1[1] = min(c1[1], x[1])
        q1+=1
    elif x[0]<sx and x[1] > sy:
        c2[0] = max(c2[0], x[0])
        c2[1] = min(c2[1], x[1])        
        q2+=1
    elif x[0]<sx and x[1] < sy:
        c3[0] = max(c3[0], x[0])
        c3[1] = max(c3[1], x[1])        
        q3+=1
    elif x[0]>sx and x[1] < sy:
        c4[0] = min(c4[0], x[0])
        c4[1] = max(c4[1], x[1])
        q4+=1
    elif x[1] == sy and x[0] > sx:
        m1[1]+=1
        m1[0] = min(m1[0], x[0])
    elif x[1] > sy and x[0] == sx:
        m2[1]+=1
        m2[0] = min(m2[0], x[1])
    elif x[1] == sy and x[0] < sx:
        m3[1]+=1
        m3[0] = max(m1[0], x[0])
    elif x[1] < sy and x[0] == sx:
        m4[1]+=1
        m4[0] = max(m4[0], x[1])        
    
#print(q1, c1, m1)
#print(q2, c2, m2)
#print(q3, c3, m3)
#print(q4, c4, m4)

pos = [0,0]
ans = 0

if ans < q1+q2+m2[1]:
    ans = q1+q2+m2[1]
    pos[1] = min(c1[1], m2[0], c2[1])
    pos[0] = sx
if ans < q2+q3+m3[1]:
    ans = q2+q3+m3[1]
    pos[1] = sy
    pos[0] = max(c2[0], c3[0], m3[0])
if ans < q3+q3+m4[1]:
    ans = q3+q4+m4[1]
    pos[1] = max(c3[1], c4[1], m4[0])
    pos[0] = sx
if ans < q4+q1+m1[1]:
    ans = q4+q1+m1[1]
    pos[1] = sy
    pos[0] = min(c4[0], c1[0], m1[0])

print(ans)
print(pos[0], pos[1])
        
    