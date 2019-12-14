import math

def create_array(size=10, mx=30):
    import random
    return random.sample(range(0,mx), size)

def counting_sort(a, base, digit):
    l = 0
    g = base-1

    t = [(i%(base**(digit+1)))//(base**digit) for i in a]

    cnt = [0]*(g-l+1)
    for i in t:
        cnt[i-l]+=1
    for i in range(1,g-l):
        cnt[i] += cnt[i-1]
    
    cnt = [0]+cnt[:-1]
    b = [0]*len(a)

    for i in range(len(a)):
        b[cnt[t[i]-l]] = a[i]
        cnt[t[i]-l]+=1
    
    return b

def heap_sort(a,base=10):
    t = int(math.log(max(a), base))+1
    b = a[:]
    for i in range(t):
        b = counting_sort(b, base, i)

    return b


a = create_array()
print(a)
print(heap_sort(a))