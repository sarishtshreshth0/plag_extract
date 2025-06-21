from collections import Counter
N,*D = map(int, open(0).read().split())
MOD = 998244353
c = Counter(D)
cnt = 1
M = max(c.keys())
ans = 1
if D[0]!=0 or c[0]!=1:
  print(0)
  import sys
  sys.exit()
while cnt<=M:
  ans *= c[cnt-1]**c[cnt]
  ans %= MOD
  cnt += 1
print(ans)