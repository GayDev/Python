n = int(input())
m = 0
d1 = 0
while n>0:
    d2 = n%10
    s = d1+d2
    if s>m:
        m = s
    d1 = n%10
    n //=10
print(m)