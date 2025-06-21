from collections import defaultdict
n,*a=map(int,open(0).read().split())
d=defaultdict(int)
s=ans=0
d[0]=1
for i in a:
    s+=i
    ans+=d[s]
    d[s]+=1
print(ans)
