from itertools import accumulate
from collections import Counter
n=int(input())
a=list(map(int,input().split()))
a=[0]+a
A=list(accumulate(a))
B=Counter(A)
ans=0
for i in B:
  ans=ans+int((B[i]*(B[i]-1)/2))
print(ans)