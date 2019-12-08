#How is an integer array sorted in place using the quicksort algorithm?

import random

a = []
for i in range(0,10):
    a.append(int(random.random()*200))

#===============================================

def quicksort(a):
    _quicksort(a,0,len(a)-1)

def _quicksort(a,begin,end):
    if end-begin > 1:
        pivot = int((end-begin)/2)
        print(a[pivot])
        a[pivot],a[end] = a[end],a[pivot]

        l = begin
        r = end-1
        while True:
            while a[l]<=a[end]:
                l+=1
            while a[r]>=a[end]:
                r-=1
            if l>r:
                break
            else:
                a[l],a[r] = a[r],a[l]
                print(a)
        
        a[end],a[l] = a[l],a[end]

        

print(a)
print()

quicksort(a)

print()
print(a)