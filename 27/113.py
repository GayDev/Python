n = int(input())
max_118 = 0
max_1 = 0
max_59 = 0
max_2 = 0
for i in range(n):
    a = int(input())
    if (a > max_118) and (a%118 == 0):
        max_118 = a
    if (a%2 != 0) and (a > max_1):
        max_1 = a
    if (a > max_2) and (a%2 == 0):
        max_2 = a
    if (a%2 != 0) and (a%59 == 0) and (a > max_59):
        max_59 = a

if (max_118+max_1 > max_59+max_2):
    if (max_118 == 0) or (max_1 == 0):
        print(0)
    else:
        print(max_118 + max_1)
else:
    if (max_59 == 0) or (max_2 == 0):
        print(0)
    else:
        print(max_59 + max_2)