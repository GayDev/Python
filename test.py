import time

for i in range(1000):
    print('{}'.format(i), end='\r')
    time.sleep(.5)