#How do you find the largest and smallest number in an unsorted integer array?

import random

a = []
for i in range(0,1000):
    a.append(int(random.random()*100000))

#==================================================

max_number = a[0]
min_number = a[0]
for i in range(0,1000):
    max_number = max(max_number,a[i])
    min_number = min(min_number,a[i])

print('Max number in the given array is: ', max_number)
print('Min number in the given array is: ', min_number)
