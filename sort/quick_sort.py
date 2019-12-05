from random import randint

def quick_sort(a):
    if len(a) < 1:
        return a
    smaller, equal, larger = [],[],[]
    pivot = a[randint(0,len(a)-1)]

    for x in a:
        if x<pivot:     smaller.append(x)
        elif x==pivot:  equal.append(x)
        else:           larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)

def partition(arr,low,high): 
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1

def quick_sort_inplace(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 

        quick_sort_inplace(arr, low, pi-1) 
        quick_sort_inplace(arr, pi+1, high) 
        