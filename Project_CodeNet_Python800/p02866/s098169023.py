import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ds = list(mapint())
mod = 998244353
from collections import Counter

c = Counter(Ds)
if Ds[0]!=0:
    print(0)
elif c[0]>1:
    print(0)
else:
    ans = 1
    for i in range(1, N):
        ans *= pow(c[i-1], c[i], mod)
        ans %= mod
    print(ans)