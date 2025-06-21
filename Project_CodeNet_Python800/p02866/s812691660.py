import sys
from collections import Counter

N = int(input())
D = list(map(int, sys.stdin.readline().rsplit()))
C = Counter(D)
mod = 998244353

if D[0] != 0 or C[0] != 1:
    print(0)
    exit()

res = 1
for i in range(1, max(D) + 1):
    if i not in C:
        print(0)
        exit()
    res *= (C[i - 1] ** C[i]) % mod

print(res % mod)
