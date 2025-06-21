import heapq
N,M=map(int,input().split())
W=[list(map(int,input().split())) for _ in range(N)]
a=[[i,0] for i in range(1,M+2)]
W.extend(a)
W.sort()
q=[]
ans=0
for i,j in W:
    if i>M+1:
        break
    if j!=0:
        heapq.heappush(q,-j)
    else:
        heapq.heappush(q,-j)
        ans-=heapq.heappop(q)
print(ans)