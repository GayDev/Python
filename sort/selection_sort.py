import random

def selection_sort(a):
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

a = []
a = random.sample(range(0,100), 50)
print('Unsorted:\t', a)
selection_sort(a)
print('Sorted:\t\t', a)