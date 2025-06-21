N=int(input())
l=list(map(int,input().split()))
ans=[0]*(N+1)
for i,j in enumerate(l):
   ans[i+1]=ans[i]+j
ans.pop(0)
import collections
f_ans=collections.Counter(ans)
ans=f_ans[0]
f_ans=[i for i in list(f_ans.values()) if i>1]
from scipy.special import comb
for i in f_ans:
   ans+=comb(i,2)
print(int(ans))