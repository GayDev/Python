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

a = [1]
print(binary_search(a,1))