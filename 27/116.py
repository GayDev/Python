def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    a = []
    b,c = 0,0
    ans = []
    for i in range(k):
        ans.append([0,0,0])

    for i in range(n):
        a.append(int(input()))

    for i in range(0,k):
        mx = a[i]
        mn = a[i]
        for j in range(i, n, k):
            if mx < a[j]:
                mx = a[j]
            if mn > a[j]:
                mn = a[j]
        ans[i][1] = mx
        ans[i][2] = mn
        ans[i][0] = mx-mn

    t = ans[0][0]
    for i in range(0,k):
        if ans[i][0] > t:
            t = ans[i][0]
            b = ans[i][1]
            c = ans[i][2]

    print(b,c)
main()