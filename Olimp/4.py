def intersection(b1, e1, b2, e2):
    l = 0
    for i in range(b1,e1):
        if i >= b2 and i < e2:
            l+= 1
    return l

s1 = input()
s2 = input()
s3 = input()

x1 = int(list(s1.split(' '))[0])
y1 = int(list(s1.split(' '))[1])
x2 = int(list(s1.split(' '))[2])
y2 = int(list(s1.split(' '))[3])

x3 = int(list(s2.split(' '))[0])
y3 = int(list(s2.split(' '))[1])
x4 = int(list(s2.split(' '))[2])
y4 = int(list(s2.split(' '))[3])

x5 = int(list(s3.split(' '))[0])
y5 = int(list(s3.split(' '))[1])
x6 = int(list(s3.split(' '))[2])
y6 = int(list(s3.split(' '))[3])


s1 = intersection(x1,x2,x3,x4)*intersection(y1,y2,y3,y4)
s2 = intersection(x1,x2,x5,x6)*intersection(y1,y2,y5,y6)
s3 = (x2-x1)*(y2-y1)
if s3 <= s1+s2:
    print('NO')
else:
    print('YES')
