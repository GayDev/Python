def create_array(size):
    import random
    return [random.randint(0,size*10) for _ in range(size)]

def find_maxes(a,c=1):
    mx = [0]*c
    for i in a:
        for j in range(c):
            if i > mx[j]:
                for k in range(1,c-j):
                    mx[-k] = mx[-k-1]
                mx[j] = i
                break
    return mx

a = create_array(20)
print(a)
print(find_maxes(a,10))
