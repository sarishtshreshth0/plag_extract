from sys import exit
from collections import Counter
mod = 998244353
n = int(input())
D = list(map(int, input().split()))
m = max(D)
C = Counter(D)
ans = 1
if C.get(0):
    if C[0] != 1 or D[0] != 0:
        print(0)
        exit()
else:
    print(0)
    exit()
for i in range(0, m):
    if C.get(i + 1):
        ans *= (C[i] ** C[i + 1]) % mod
        ans %= mod
    else:
        print(0)
        exit()

print(ans)