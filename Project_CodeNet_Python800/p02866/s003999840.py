N = int(input())
D = list(map(int, input().split()))

mod = 998244353

from collections import Counter, deque

def solve(N,D):
    if D[0]!=0:
        return 0
    c = Counter(D)
    if c[0]>1:
        return 0
    ans = 1
    m = max(D)
    for i in range(1,m):
        # if c[i]==0:
        #     ans = 0
        #     continue
        ans *= pow(c[i],c[i+1],mod)
        ans %= mod
    return ans

print(solve(N,D))