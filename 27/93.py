n = int(input())

buf = []
l_d = [0]*10
ans = 0

for i in range(6):
    buf.append(int(input()))

for i in range(n-6):
    first = buf[i%6]
    l_d[first%10] += 1

    x = int(input())        # 3 = 1*3 = 3*1
    if x%10==1:
        ans += l_d[3]
    elif x%10==3:
        ans += l_d[1]
    elif x%10==7:
        ans += l_d[9]
    elif x%10==9:
        ans += l_d[7]
    
    buf[i%6] = x

print(ans)