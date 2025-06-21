from collections import defaultdict
import sys
MOD=998244353
N=int(input())
dlist=list(map(int,input().split()))

if dlist[0]!=0:
  print(0)
  sys.exit(0)
  
ddic=defaultdict(int)
for d in dlist:
  ddic[d]+=1
  
if ddic[0]!=1:
  print(0)
  sys.exit(0)
  
max_d=max(dlist)
answer=1
for d in range(1,max_d+1):
  if ddic[d]==0:
    print(0)
    sys.exit(0)
    
  term=pow(ddic[d-1],ddic[d],MOD)
  answer*=term
  answer%=MOD
  
print(answer)