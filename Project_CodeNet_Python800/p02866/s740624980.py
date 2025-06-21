from collections import Counter
n = int(input())
l = list(map(int,input().split()))
c = Counter(l)
mod = 998244353
if l.count(0) != 1 or l[0] != 0:
    print(0)
    exit()
ans = 1
for i in l[1:]:
    ans *= c[i-1]
    ans %= mod
print(ans%mod)
