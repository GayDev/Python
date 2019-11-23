def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a = int(input())
b = int(input())
p = 1
for i in range(a,b+1):
    p *= i

p = sum_digits(p)
while p>=10:
    p = sum_digits(p)

print(p)
