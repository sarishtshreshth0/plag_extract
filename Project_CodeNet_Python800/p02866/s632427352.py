n=int(input())
d=list(map(int,input().split()))

if d[0]!=0:
  print(0)
  exit(0)
  
m=max(d)
counts=[0]*(m+1)

import collections
counter=collections.Counter(d)

for key,val in counter.items():
  counts[key]=val
if counts[0]!=1:
  print(0)
  exit(0)
ans=1
div=998244353
for i in range(1,len(counts)):
  ans*=pow(counts[i-1],counts[i],div)
  ans%=div
  
print(ans)