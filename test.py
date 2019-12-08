import math

def is_prime(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if a % i == 0:
            return False
    return True

print(is_prime(int(input())))