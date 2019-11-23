n = int(input())
positive = []
inp = input()
for i in range(0,n):
    cur_number = int(inp.split(' ')[i])
    if cur_number < 0:
        print(cur_number, end=' ')
    else:
        positive.append(cur_number)

for i in range (0,len(positive)):
    print(positive[i], end=' ')

print()