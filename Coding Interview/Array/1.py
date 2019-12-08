#How do you find the missing number in a given integer array of 1 to 100?
import random

a = []
missing_number = int(random.random()*100)
for i in range(0, 100):
    if i != missing_number:
        a.append(i)
print(missing_number)
#=================================================

find = False
i = 0
while find==False:
    if a[i+1]-a[i] != 1:
        find = True
        print('Missing element is: ', a[i]+1)
    i += 1
