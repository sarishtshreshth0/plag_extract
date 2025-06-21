from collections import Counter
import sys
MOD = 998244353

n = int(input())
a = list(map(int,input().split()))

aa = Counter(a)
ma = max(aa)

def po(x,n):
    k = 1
    for i in range(n):
        k = k*x % MOD
    return k

if aa[0] != 1 or a[0] != 0:
    print(0)
    sys.exit()
    
ans = 1
for i in range(ma):
    c,d = aa[i],aa[i+1]
    if c == 0 or d == 0:
        print(0)
        sys.exit()
    else:
        ans = ans * po(c,d) % MOD
        
print(ans)