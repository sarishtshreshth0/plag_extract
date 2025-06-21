import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())
D = list(map(int, sys.stdin.readline().rstrip().split()))
mod = 998244353

if D[0] != 0 or 0 in D[1:]:
    print(0)
    exit()

d_cnt = sorted(Counter(D).items())

ans = 1
par = 1
prev = 0
for k, v in d_cnt:
    if k > 0:
        if prev + 1 == k:
            ans *= pow(par, v, mod)
            ans %= mod
            par = v
            prev = k
        else:
            print(0)
            exit()
print(ans)