import heapq

n,m=map(int,input().split())
task=[[0] for _ in range(m+1)]

for i in range(n):
    a,b=map(int,input().split())
    if a<=m:
        task[a].append(b)

task=task[::-1]

tmp=[]
heapq.heapify(tmp)
ans=0

for i in range(m,-1,-1):
    cnt=0
    for j in task[i]:
        heapq.heappush(tmp,-j)
    cnt=heapq.heappop(tmp)
    ans-=cnt
print(ans)
