import random
import time

def create_array(size):
    #return [random.randint(0,size*10) for _ in range(size)]
    return [3]*size

def find_sum(a):
    s = 0
    for i in range(len(a)):
        s +=  a[i]
    
    return s

def stupid_function(a):
    return a[0] + a[1]

print('Maximum array size: ' ,end='')
n = int(input())
print('Tries: ', end='')
t = int(input())

print('\n| SIZE\t|   TIME (ms)')
print('-'*20)
for i in range(1,n+1):
    tm = [0]*t
    a = create_array(2**i)

    for j in range(t):
        t0 = time.time()
        find_sum(a)
        t1 = time.time()
        tm[j] = (t1-t0)*1000

    print('| 2^%d\t|   %d' % (i, sum(tm)/t))
    print('-'*20)
