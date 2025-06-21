from collections import deque
n=int(input())
e=[]
edge=[[] for _ in range(n)]
for i in range(n-1):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)
    e.append(str(x-1)+" "+str(y-1))
par=[0]*n #自分の親と何番でつながっているか
visited=[0]*n
visited[0]=1
que=deque([0])
ans=dict()
K=0
while que:
    now=que.popleft()
    color=1
    for x in edge[now]:
        if visited[x]:
            continue
        visited[x]=1
        que.append(x)
        if color==par[now]:
            color+=1
        par[x]=color
        ans[str(min(x,now))+" "+str(max(x,now))]=color
        color+=1
print(max(ans.values()))
for i in e:
    print(ans[i])