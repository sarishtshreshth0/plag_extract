from heapq import heapify,heappop,heappush
N,M=map(int,input().split())
item=[list(map(int,input().split())) for i in range(N)]
item.sort(key=lambda x:x[0])
que=[]
heapify(que)
ans=0
j=0
for i in range(1,M+1):
    while(j<N and item[j][0]<=i):
        heappush(que,-item[j][1])
        j+=1
    if que:
        ans+=-heappop(que)
print(ans)