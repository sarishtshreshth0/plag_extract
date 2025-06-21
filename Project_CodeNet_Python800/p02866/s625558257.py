mod = 998244353
N = int(input())
D = list(map(int,input().split()))
from collections import Counter
if D[0] != 0 or 0 in D[1:]:
    print(0)
else:
    dc1 = Counter(D[1:])
    dc = [0 for i in range(max(D))]
    for k,v in dc1.items():
        dc[k-1] = v
    ans = 1
    for i in range(1,len(dc)):
        if dc[i] == 0:
            ans = 0
            break
        ans = (ans*(dc[i-1]**dc[i]))%mod
    print(ans)