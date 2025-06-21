n = int(input())
d = list(map(int,input().split()))
m = 998244353
import collections
c = collections.Counter(d)
if c[0] == 1 and d[0] == 0:
    ans = 1
else:
    ans = 0
d = sorted(d)
for i in range(1,n):
    ans *= c[d[i]-1]
    ans %= m
print(ans)