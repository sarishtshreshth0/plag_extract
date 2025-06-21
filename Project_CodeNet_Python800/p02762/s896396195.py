from collections import deque
N,M,K=map(int,input().split())
friend=[deque([]) for _ in range(N+1)]
block=[deque([]) for _ in range(N+1)]
for i in range(M):
  a,b=map(int,input().split())
  friend[a].append(b)
  friend[b].append(a)
for i in range(K):
  c,d=map(int,input().split())
  block[c].append(d)
  block[d].append(c)
stack=deque()
group=[-1]*(N+1)
visited=[-1]*(N+1)
dic={}
for i in range(1,N+1):
  stack.append(i)
  main=i
  cnt=0
  while len(stack)>0:
    now=stack.popleft()
    if group[now]!=-1:
        continue
    stack.extend(friend[now])
    group[now]=main
    cnt+=1
  if cnt!=0:
    dic[main]=cnt

for i in range(1,N+1):
  ans=dic[group[i]]
  ans-=1
  ans-=len(friend[i])
  for j in block[i]:
    if group[j]==group[i]:
      ans-=1
  print(ans)