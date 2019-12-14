import random

def create_array(size=10, mx=30):
    return random.sample(range(0,mx), size)

def counting_sort(a):
    l = None
    g = None

    for i in a:
        if l==None or i<l:
            l=i
        elif g==None or i>g:
            g=i

    cnt = [0]*(g-l+1)
    for i in a:
        cnt[i-l]+=1
    for i in range(1,g-l):
        cnt[i] += cnt[i-1]
    
    cnt = [0]+cnt[:-1]
    b = [0]*len(a)

    for i in a:
        b[cnt[i-l]] = i
        cnt[i-l]+=1
    
    return b

a = create_array(20,99)
print(counting_sort(a))