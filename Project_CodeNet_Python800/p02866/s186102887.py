mod = 998244353
n = int(input())
d = list(map(int,input().split()))
from collections import Counter
c = Counter(d)
ans = 1
b = 1
if c[0]!=1 or d[0]!=0:ans = 0 
for i in range(max(d)+1):
    ans = (ans*b**c[i])%mod
    b = c[i]
print(ans)