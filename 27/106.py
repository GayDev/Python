n = int(input())

cur_length = 1
max_length = 1

prev = list(map(int, input().split()))
for i in range(1,n):
    cur = list(map(int, input().split()))

    if prev[1] == cur[0]:
        cur_length += 1
    elif prev[1] == cur[1]:
        cur = cur[::-1]
        cur_length += 1
    else:
        prev = prev[::-1]
        if prev[1] == cur[0]:
            cur_length += 1
        elif prev[1] == cur[1]:
            cur = cur[::-1]
            cur_length += 1
        else:
            cur_length = 1

    
    if cur_length > max_length:
        max_length = cur_length

    prev = cur

print(max_length)