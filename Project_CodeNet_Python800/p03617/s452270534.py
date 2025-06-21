q,h,s,d = map(int,input().split())
n = int(input())
a=min(q*8,h*4,s*2,d)
b=min(q*4,h*2,s)
ans = 0
if n%2==1:
    ans += b
    ans += min(b*(n-1),a*(n//2))
else:
    ans += min(b*n,a*(n//2))
print(ans)