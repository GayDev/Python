import random
import time

def create_array(size=10, mx=100):
    return random.sample(range(0,mx), size)

def merge(a,b):
    c = []
    i,j = 0,0

    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c.extend(a[i:])
    elif j < len(b):
        c.extend(b[j:])

    return c

def binary_interval_search(arr,s,b=None,e=None):
    if b==None:
        b = 0
    if e==None:
        e = len(arr)-1

    if e-b <= 1:
        if s <= arr[b]:
            return b
        elif s >= arr[e]:
            return e+1
        else:
            return e

    pivot = (b+e)//2
    if s > arr[pivot]:
        return binary_interval_search(arr,s,pivot,e)
    elif s < arr[pivot]:
        return binary_interval_search(arr,s,b,pivot)
    else:
        return pivot+1

def insertion_sort(a):
    s = [a[0]]
    for i in range(1,len(a)):
        t = binary_interval_search(s,a[i])
        s = s[:t]+[a[i]]+s[t:]
    return s

def timsort(b, run=5):
    a = b
    for i in range(0,len(a),run):
        a[i:i+run] = insertion_sort(a[i:i+run])
    for i in range(run,len(a),run):
        a[0:i+run] = merge(a[0:i], a[i:i+run])

    return b

n = int(input())    
print('SIZE\t\tITME (secs)')
print('_'*30)
for i in range(1,n+1):
    a = create_array(10**i, (10**i) * 10)
    t0 = time.time()
    timsort(a)
    t1 = time.time()
    print('10^%d\t\t%.7f' % (i, t1-t0))