from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

n=int(input())
d=lnii()

mod=998244353

c=Counter(d)
max_key=max(d)

if d[0]!=0 or c[0]!=1:
  print(0)
  exit()

ans=1
patterns=1
for i in range(max_key+1):
  p_num=c[i]
  ans*=patterns**p_num
  ans%=mod
  patterns=p_num

print(ans)