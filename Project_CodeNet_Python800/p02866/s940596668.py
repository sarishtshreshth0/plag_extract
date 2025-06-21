from collections import Counter
n = int(input())
d = list(map(int,input().split()))
c = Counter(d)
mod=998244353
if d[0]==1:
    print(0)
else:
    D = 1
    for i in d[1:]:
        D = (D*c[i-1])%mod
    print(D)