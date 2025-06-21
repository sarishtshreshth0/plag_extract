n=input()
r=input()
r=r.split(" ")
r=sorted(r)
a=list(map(int,r))

d=dict()

ans=0
count=0

from collections import defaultdict
d = defaultdict(lambda: 0, d)

for i in a:
    d[i]=d.get(i,0)+1

p=0
while(p<100010):
    count=d[p-1]+d[p]+d[p+1]
    p=p+1
    if(count>ans):
        ans=count
print(ans)