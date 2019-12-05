import random

def binary_interval_search(arr,s,b=None,e=None):
    if b==None:
        b = 0
    if e==None:
        e = len(arr)-1

    if e-b<=1:
        return b

    pivot = (b+e)//2

    if s > arr[pivot]:
        return binary_interval_search(arr,s,pivot+1,e)
    elif s < arr[pivot]:
        return binary_interval_search(arr,s,b,pivot-1)
    else:
        return pivot+1

def create_sorted_array(size=10, step=5):
    t = 0
    a = []
    for _ in range(size):
        a.append(random.randint(t, t+step))
        t+= step
    return a

a = create_sorted_array()
print(a)
t = binary_interval_search(a,0)
print('[%d:\t%d;\t%d]' % (t,a[t-1],a[t]))