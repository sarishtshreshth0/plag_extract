from heapq import heappop, heappush

n,m=map(int,input().split())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a>m:continue
    l.append((a,b))

l.sort(reverse=True)

q=[]
ans=0

for i in range(1,m+1):
    while l and l[-1][0]<=i:
        a,b=l.pop()
        heappush(q,-b)
    if q:
        b=-heappop(q)
        ans+=b
print(ans)
