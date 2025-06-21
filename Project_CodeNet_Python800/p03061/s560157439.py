from fractions import gcd
n=int(input())
a=list(map(int,input().split()))
r=[a[-1]]
l=[a[0]]
for i in range(1,n-1):
    l.append(gcd(l[i-1],a[i]))
    r.append(gcd(r[i-1],a[-1-i]))
ans=r[-1]    
for i in range(n-2):
    ans=max(ans,gcd(l[i],r[-2-i]))
ans=max(ans,l[-1])
print(ans)