import itertools
import collections
n=int(input())
a=list(map(int,input().split()))
a=list(itertools.accumulate(a))
a.insert(0,0)
a=collections.Counter(a)
ans=0
for i in a:
  ans+=(a[i]-1)*a[i]//2
print(ans)