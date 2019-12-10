n = int(input())
r = [[0]*3]
cur_seq = 0
ans = 0


for i in range(n):                              #n
    x = int(input())                            #1
    if x!=0:
        k = x%3                                 #1
        r[cur_seq][k] = max(r[cur_seq][k], x)   #1
        if cur_seq != 0:
            pair_k = (3-k)%3                    #1
            for j in range(cur_seq):            #c_s
                if x + r[j][pair_k] > ans:
                    ans = x + r[j][pair_k]      #1
    else:
        cur_seq += 1
        r.append([0]*3)
    

print(ans)