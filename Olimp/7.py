def func(k,a):
    if len(a)>=k+1:
        for i in range(len(a)-k-1,len(a)):
            if a[i]:
                return i + 1 + func(k,a[:(i-k)])
        for i in range(1,n):
            if a[-i]:
                cost = len(a)-i+1
                for j in range(len(a)-i+k+i, len(a)):
                    cost += j+1
                return cost + func(k,a[:(i-k)])
    # else:
    #     for i in range(0,len(a)):
    #         if a[i]:
    #             return i + 1 + func(k,a[:(i-k)])
    #     for i in range(1,n):
    #         if a[-i]:
    #             cost = len(a)-i+1
    #             for j in range(len(a)-i+k+i, len(a)):
    #                 cost += j+1
    #             return cost + func(k,a[:(i-k)])
            


n,k = input().split(' ')
n = int(n)
k = int(k)
s = input()
a = []
is_connected = []
for i in range(0,n):
    if s[i] == '0':
        a.append(False)
    else:
        a.append(True)
    is_connected.append(False)

print(func(k,a))