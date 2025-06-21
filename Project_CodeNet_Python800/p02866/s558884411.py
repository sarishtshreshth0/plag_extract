#B
import sys
from collections import Counter
n=int(input())
d=list(map(int,input().split()))
e=Counter(d)
mod=998244353
if d[0]!=0 or e[0]!=1:
    print(0)
    sys.exit()
ans=1
for i in range(2,n):
    ans*=pow(e[i-1],e[i],mod)
    ans%=mod
print(ans%mod)