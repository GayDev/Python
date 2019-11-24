n = int(input())
t = int(input())
a = []
b = []
for i in range(0,n):
    inp = input()
    a.append(int(inp.split(' ')[0]))
    b.append(int(inp.split(' ')[1]))
    a_length += a[i]
    b_length += b[i]


for i in range(0,n):
    path_length = 0
    for j in range(0,i):
        path_length += a[j]
    for k in range(i,n):
        path_length += b[k]
    if i == 0:
        min_length = path_length
    else:
        min_length = min(min_length, path_length)

print(min_length+t)