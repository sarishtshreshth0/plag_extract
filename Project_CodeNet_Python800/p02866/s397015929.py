from collections import Counter
N = int(input())
d = list(map(int, input().split()))

MOD = 998244353

dn = Counter(d)
ans = 1
if dn[0] != 1 or d[0] != 0: ans = 0
else:
    for i in range(1, max(d)+1):
        ans *= (dn[i-1]**dn[i])
        ans %= MOD
    
print(ans)