m1,m2 = -1,-1
n = int(input())
odd,even = [],[]
for i in range(n):
    t = int(input())
    if t%2 == 0:
        even.append(t)
    else:
        odd.append(t)

for i in range(len(even)):
    if (even[i] % 3 == 0) and (even[i] > m1):
        m1 = even[i]
+
for i in range(len(odd)):
    if (odd[i] % 3 == 0) and (odd[i] > m2):
        m2 = odd[i]

if (m1 == -1) and (m2 == -1):
    print(0)
elif (m1 * max(odd)) > (m2 * max(even)):
    print(m1,max(odd))
else:
    print(m2,max(even))