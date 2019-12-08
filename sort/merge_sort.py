import random

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

def merge_sort(a):
    if len(a) <= 1:
        return a
    left,right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    return merge(left,right)

a = create_array(20)
print(a)
print(merge_sort(a))