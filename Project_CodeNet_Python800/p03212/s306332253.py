n=int(input())
ans=0
import itertools
for i in range(3,10):
  blist=itertools.product(['3','5','7'], repeat=i)
  for j in blist:
    if '3' in j and '5' in j and '7' in j:
      if int(''.join(j))<=n:
        ans+=1
print(ans)