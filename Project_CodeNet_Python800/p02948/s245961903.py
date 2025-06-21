import heapq
import queue

n,m=map(int,input().split())
L=[]
for inp in range(n):
    a,b=map(int,input().split())
    L.append((a,b))
L.sort(reverse=True)

pq=[]
heapq.heapify(pq)

    
ans=0
for i in range(1,m+1):
    while len(L)>0 and L[-1][0]==i:
        heapq.heappush(pq,L.pop()[1]*-1)
    #print(pq)
    if len(pq)==0:
        continue
    else:    
        ans-=heapq.heappop(pq)

print(ans)


