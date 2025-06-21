import collections

n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
ans=0
for k,v in c.items():
    ans=max(ans,(v + c.get(k-1,0) + c.get(k+1,0)))
print(ans)