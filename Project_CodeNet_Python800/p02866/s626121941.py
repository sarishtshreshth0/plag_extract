N=int(input())
*D,=map(int,input().split())
M=max(D)
from collections import*
C=Counter(D)

ans=1
now=C[1]
for i in range(2,M+1):
    ans*=pow(now,C[i],998244353)
    ans%=998244353
    now=C[i]

if D[0]!=0:
    ans=0
if 0 in D[1:]:
    ans=0
print(ans)