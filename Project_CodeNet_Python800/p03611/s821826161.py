from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from collections import Counter

n=int(input())
a=lnii()

c=Counter(a)
a_max=max(a)

ans=0
for i in range(a_max+1):
  t_ans=c[i-1]+c[i]+c[i+1]
  ans=max(ans,t_ans)

print(ans)
