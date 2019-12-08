import random
import time
import math

def create_array(size):
    return [random.randint(0,size*10) for _ in range(size)]
    #return [3]*size

def create_sorted_array(size, step=5):
    t = 0
    a = []
    for _ in range(size):
        a.append(random.randint(t, t+step))
        t+= step
    return a


def find_sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

def binary_search(a,s,b=None,e=None):
    if b==None:
        b = 0
    if e==None:
        e=len(a)-1

    p = (b+e)//2
    if s > a[p]:
        return binary_search(a,s,p+1,e)
    if s < a[p]:
        return binary_search(a,s,b,p-1)
    return p


def stupid_function(a):
    return a[0] + a[1]

def quick_sort(a):
    if len(a) < 1:
        return a
    smaller, equal, larger = [],[],[]       # 1
    pivot = a[random.randint(0,len(a)-1)]          # 1

    for x in a:                             # n
        if x<pivot:     smaller.append(x)
        elif x==pivot:  equal.append(x)
        else:           larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)     # 3n

def bubble_sort(a):
    arr = a
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def is_prime(a):
    q = True
    for i in range(1,int(math.sqrt(a))+1):
        if a % i == 0:
            q = False
    return q

print('Minimum array size: ', end='')
m = int(input())
print('Maximum array size: ', end='')
n = int(input())
print('Passes: ', end='')
t = int(input())
print('Step: ',end='')
s = int(input())

import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'SIZE')
for i in range(0,t):
    sheet1.write(0, i+1, 'PASS %d' % (i+1))
r = 0

for i in range(m,n+1,s):
    r += 1
    print('%.1f' % (100*(i-m)/(n-m)), end='')
    print('%', end='')
    print('\tCurrent size: %d' % i, end='')
    sheet1.write(r, 0, 2**i)
    
    for j in range(t):
        t0 = time.time_ns()
        is_prime(2**i)
        t1 = time.time_ns()
        sheet1.write(r, j+1, (t1-t0)/(10**6))
    print('\tDone!\n' + '_'*50)

wb.save('speed_test.xls')
print('Saved!')