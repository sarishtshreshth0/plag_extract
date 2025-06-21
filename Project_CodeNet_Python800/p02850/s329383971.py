from collections import deque
n=int(input())
arr=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    arr[a-1].append([b-1,i])
    arr[b-1].append([a-1,i])

que=deque([0])
ans=[0]*(n-1)
par=[0]*n
par[0]=-1
while que:
    x=que.popleft()
    p=par[x]
    color=1
    for tup in arr[x]:
        if p==color:
            color+=1
        if ans[tup[1]]==0:
            ans[tup[1]]=color
            par[tup[0]]=color
            color+=1
            que.append(tup[0])
print(max(ans))
print(*ans,sep='\n')