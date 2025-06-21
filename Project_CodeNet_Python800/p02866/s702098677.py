N = int(input())
*D, = map(int, input().split())
MOD = 998244353

import collections
dic = collections.Counter(D)

flag = 1 if dic[0] != 1 or D[0] != 0 else 0
ans = 1
for d in range(1, max(D)+1):
    ans *= pow(dic[d-1], dic[d], MOD)
    ans %= MOD

if flag: 
    print(0)
else:
    print(ans)