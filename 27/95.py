n = int(input())

buf = []
l_d = [0]*10
ans = 0

for i in range(4):
    buf.append(int(input()))

for i in range(n-4):
    first = buf[i%4]
    l_d[first%10] += 1

    x = int(input())        # 1 = 1*1 = 3*7 = 7*3 = 9*9
    if x%10==1:
        ans += l_d[1]
    elif x%10==3:
        ans += l_d[7]
    elif x%10==7:
        ans += l_d[3]
    elif x%10==9:
        ans += l_d[9]
    
    buf[i%4] = x

print(ans)