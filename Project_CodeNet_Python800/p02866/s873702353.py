from collections import Counter

N = int(input())
D = list(map(int,input().split()))
C = Counter(D)
mod = 998244353
ans = 1
D_max = max(D)

if D[0] != 0 or C[0] != 1:
    print(0)
    exit()
"""
def make_factorial_table(n):
    result = [0] * (n+1)
    result[0] = 1
    for i in range(1,n+1):
        result[i] = result[i-1] * i % mod
    return result

def nCr(n,r):
    return fact[n] * pow(fact[n-r],mod-2,mod) * pow(fact[r],mod-2,mod) % mod

fact = make_factorial_table(2*N)
"""

for i in D[1:]:
    ans *= C[i-1]
    ans %= mod
print(ans)