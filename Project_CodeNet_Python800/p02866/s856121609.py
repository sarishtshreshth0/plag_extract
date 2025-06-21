n=int(input())
d=[int(j) for j in input().split()]
if d[0]!=0:
    print(0)
    exit()
mod=998244353
import collections
c=collections.Counter(d)
l=c.most_common()
l.sort()
ans=1
tmp=0
for i in range(len(l)):
    if i==0:
        if l[i][1]!=1:
            print(0)
            exit()
        tmp=1
        continue
    if l[i][0]!=i:
        print(0)
        exit()
    ans=(ans*pow(tmp,l[i][1],mod))%mod
    tmp=l[i][1]
print(ans)