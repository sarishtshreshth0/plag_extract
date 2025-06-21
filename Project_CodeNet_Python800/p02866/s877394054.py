
n=int(input())
d=list(map(int,input().split()))

from collections import Counter
c=Counter(d)

mod=998244353
ans=1
key=set(c.keys())
if d[0]==0 and c[0]==1 and set(range(len(key))) == key:
    for i in range(len(key)):
        #print(i,c[i],c[i+1],c[i]**c[i+1])
        ans=ans*c[i]**c[i+1] %mod
else:
    ans=0
print(ans)