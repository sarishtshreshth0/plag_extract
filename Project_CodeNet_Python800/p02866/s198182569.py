N = int(input())
D = list(map(int,input().split()))
if D[0] != 0:
    print(0)
    exit()
from collections import Counter
ctr = Counter(D)
if ctr[0] > 1:
    print(0)
    exit()

MOD = 998244353
ans = 1
for i in range(len(ctr)-1):
    ans *= pow(ctr[i], ctr[i+1], MOD)
    ans %= MOD
print(ans)