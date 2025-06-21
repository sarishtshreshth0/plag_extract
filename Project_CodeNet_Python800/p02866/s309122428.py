from collections import Counter

N = int(input())
D = list(map(int, input().split()))

mod = 998244353
c = Counter(D)
m = max(c.keys())

if D[0] == 0 and c[0] == 1:
    ans = 1
    for i in D[1:]:
        ans *= c[i-1]
        ans %= mod
    print(ans)
else:
    print(0)
