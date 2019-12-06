import random, time

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

def find(arr,s):
    if s<=arr[0]:
        return 0
    elif s >= arr[-1]:
        return len(arr)
    
    for i in range(1,len(arr)):
        if s>= arr[i-1] and s <= arr[i]:
            return i
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
        #t = find(s,a[i])
        s = s[:t]+[a[i]]+s[t:]
    return s

def selection_sort(b):
    a = b
    sorted_length = 0
    while sorted_length < len(a):
        mn = a[sorted_length]
        t = sorted_length
        for i in range(sorted_length,len(a)):
            if a[i] < mn:
                mn = a[i]
                t = i
        a[sorted_length],a[t] = a[t],a[sorted_length]
        sorted_length+=1
    return a

def quick_sort(a):
    if len(a) < 1:
        return a
    smaller, equal, larger = [],[],[]
    pivot = a[random.randint(0,len(a)-1)]

    for x in a:
        if x<pivot:     smaller.append(x)
        elif x==pivot:  equal.append(x)
        else:           larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)

def timsort(b, run=5):
    a = b
    for i in range(0,len(a),run):
        a[i:i+run] = insertion_sort(a[i:i+run])
    for i in range(run,len(a),run):
        a[0:i+run] = merge(a[0:i], a[i:i+run])

    return b

def create_array(size=10, mx=30):
    return random.sample(range(0,mx), size)

n = int(input())
print('SIZE\t\t\tMERGE\t\t\tINSERTION\t\tSELECTION\t\tQUICKSORT\t\tTIMSORT\t\t\tSORT')
print('_'*150)
for i in range(1,n+1):
    a = create_array(2**i,(2**i)*10)
    t0 = time.time()
    merge_sort(a)
    t1 = time.time()
    insertion_sort(a)
    t2 = time.time()
    selection_sort(a)
    t3 = time.time()
    quick_sort(a)
    t4 = time.time()
    timsort(a)
    t5 = time.time()
    a.sort()
    t6 = time.time()

    print('2^%d\t\t\t%.10f\t\t%.10f\t\t%.10f\t\t%.10f\t\t%.10f\t\t%.10f' % (i,t1-t0,t2-t1,t3-t2,t4-t3,t5-t4,t6-t5))