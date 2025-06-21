import collections

n = int(input())
d = list(map(int,input().split()))
mod = 998244353

ans = 0
c = collections.Counter(d)
if c[0] == 1 and d[0] == 0:
    ans = 1
for i in range(1,max(d)+1):
    if c[i] == 0:
        ans = 0
        break
    ans *= pow(c[i-1],c[i],mod)
    ans %= mod
print(ans%mod)