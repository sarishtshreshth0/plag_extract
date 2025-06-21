import math
import sys

n=int(input())

d=list(map(int,input().split()))

if d[0]!=0 or 0 in d[1:]:
    print(0)
    sys.exit()

lis=[0 for i in range(n)]

for i in range(n):
    lis[d[i]]+=1

for i in range(1,n-1):
    if lis[i]==0 and lis[i+1]!=0:
        print(0)
        sys.exit()
s=1

i=0
while i+1<=n-1 and lis[i+1]!=0:
    s=(s*pow(lis[i],lis[i+1],998244353))%998244353
    i+=1
print(s)
