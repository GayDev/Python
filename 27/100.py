def diagonals(a):
    return (a>3)*int(a*(a-3)/2)

n = int(input())    # 0 -> 3 6 9 ...
                    # 1 -> 2 5 8 ...
                    # 2 -> 1 4 7 ...

t = list(map(int, input().split()))
a, b, c = [0,0],[0,0],[0,0]

for i in range(1,n+1):
    x = t[i-1]
    if i%3==0:
        if x%3==0:
            a[0]+=1
        else:
            a[1]+=1

    elif i%3==1:
        if x%3==0:
            b[0]+=1
        else:
            b[1]+=1

    else:
        if x%3==0:
            c[0]+=1
        else:
            c[1]+=1

ans = a[0]*a[1] + a[0] + diagonals(a[0]) + \
      b[0]*b[1] + b[0] + diagonals(b[0]) + \
      c[0]*c[1] + c[0] + diagonals(c[0])


print(ans)
# 4 8 6 7 4 6 8 6 9 8 3 2 7 1 8 4 4 1 6 7 1 3 8 5 6 2 5 5 9 6