import collections

N = int(input())
D = list(map(int, input().split()))
mod = 998244353

if(D[0] != 0):
    print(0)
else:
    c = collections.Counter(D)
    ans = 1
    for val in D[1:]:
        ans = (ans*c[val-1])%mod
    print(ans)