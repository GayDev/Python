def GCD(a,b):
    while b:
        a,b = b,a%b
    return a

a = int(input())
b = int(input())
print(GCD(a,b))