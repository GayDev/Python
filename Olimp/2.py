n = int(input())
s = input()
i = 0
ans=0
while i < n:
    if s[i] == s[i+1]:
        ans+=1
        if s[i] == 'a':
            s = s[:i] + 'b' + s[(i+1):]
        else:
            s = s[:i] + 'a' + s[(i+1):]
    i += 2

print(ans)
print(s)