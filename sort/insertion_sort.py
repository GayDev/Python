import random
import time

def create_array(size=10, mx=30):
    return random.sample(range(0,mx), size)
def create_sorted_array(size=10, step=5):
    t = 0
    a = []
    for _ in range(size):
        a.append(random.randint(t, t+step))
        t+= step
    return a

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
        
n = int(input())
print('SIZE\t\tTIME (sec)')
print('_'*30)
for i in range(1,n+1):
    a = create_array(10**i,(10**i)*100)
    t0 = time.time()
    a = insertion_sort(a)
    t1 = time.time()
    print('10^%d\t\t%.5f' % (i,t1-t0))
