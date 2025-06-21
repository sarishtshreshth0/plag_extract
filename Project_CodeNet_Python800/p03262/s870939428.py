import math

n,f = map(int,input().split())
x = list(map(int,input().split()))
x.append(f)
k = min(x)
ans = max(x)-k
for i in range(n+1):
    if math.gcd(ans, x[i]-k) < ans:
        ans = math.gcd(ans, x[i]-k)
print(ans)
