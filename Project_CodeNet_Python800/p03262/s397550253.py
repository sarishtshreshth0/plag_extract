def gcd(p,q):
    if p%q==0: return q
    else: return gcd(q,p%q)
n,x = map(int,input().split())
a = list(map(int,input().split()))
b = [abs(x-i) for i in a]
ans = b[0]
for i in range(1,n):
    ans = min(ans,gcd(ans,b[i]))
print(ans)