a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

ans = 0
if e>f:
    ans += min(a,d)*e
    d-=min(a,d)
    ans+=min(b,c,d)*f
    
else:
    ans+=min(b,c,d)*f
    d-=min(b,c,d)
    ans+=min(a,d)*e
    
print(ans)