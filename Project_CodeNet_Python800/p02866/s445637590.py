import sys
from collections import Counter
n = int(input())
D = list(map(int,input().split()))
if D[0] != 0 or D.count(0) != 1:
    print(0)
    sys.exit()
D = Counter(D)
L = sorted(D.items())
pk = 0
pv = 1
ans = 1
for i,j in L:
    if i == 0:
        continue
    if i != pk+1:
        print(0)
        break
    ans *= pv**j
    ans %= 998244353
    pk = i
    pv = j
else:
    print(ans)