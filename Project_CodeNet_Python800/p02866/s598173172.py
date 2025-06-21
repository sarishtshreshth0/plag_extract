MOD=998244353
from collections import Counter
N=int(input())
D=list(map(int,input().split()))
if D[0]!=0:
    print(0)
    exit()
c=sorted(Counter(D[1:]).most_common(),key=lambda x:x[0])
ans=1
for i in range(1,len(c)):
    if(c[i][0]!=i+1):
        print(0)
        exit()
    ans=(ans*pow(c[i-1][1],c[i][1],MOD))%MOD
print(ans)