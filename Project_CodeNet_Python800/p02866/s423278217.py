import collections
n = int(input())
d = list(map(int,input().split()))
ma = max(d)
mod = 998244353

if d[0] != 0:
    print(0)
    exit()

p = [0 for i in range(ma+1)]

for i in range(n):
    p[d[i]] += 1

if p[0] != 1:
    print(0)
    exit()
else:
    ans = 1
    for i in range(1,ma+1):
        ans *= (p[i-1]**p[i])%mod
        ans %= mod
    
    print(ans)