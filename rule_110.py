import random
import os
import time

def print_gen(a):
    for i in range(len(a)):
        if a[i]==0:
            print(' ', end='')
        else:
            print('@', end='')
    print()

#w, h = subprocess.check_output(['stty', 'size']).split()
h = 900
w = 900

chance = float(input())
os.system('clear')
curr_gen = []
mp = [0,1,0,0,1,0,1,1]
for i in range(w):
    curr_gen.append(random.random() <= chance)
# curr_gen = [0]*w
# curr_gen[-1] = 1

while True:
    print_gen(curr_gen)
    next_gen = [0]*w

    for i in range(1,w-1):
        n = 4*curr_gen[i-1] + 2*curr_gen[i] + curr_gen[i+1]
        next_gen[i] = mp[n]
    
    n = 4*curr_gen[-1] + 2*curr_gen[0] + curr_gen[1]
    next_gen[0] = mp[n]
    n = 4*curr_gen[-2] + 2*curr_gen[-1] + curr_gen[0]
    next_gen[-1] = mp[n]
    curr_gen = next_gen[:]
    time.sleep(0.07)

