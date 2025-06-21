from collections import deque
n,m,k=map(int,input().split())
fr=[[]]
for i in range(n-1):
  fr.append([])
for i in range(m):
  a,b=map(int,input().split())
  fr[a-1].append(b)
  fr[b-1].append(a)

belong=[0]*n
anslist=[0]*n
count=0
def bfs(k):
  global count
  if belong[k-1]==0:
    count+=1
    use=deque()
    use.append(k)
    ans=0
    aldic={}
    while use:
      check=use.popleft()
      if check not in aldic:
        aldic[check]=1
        for x in fr[check-1]:
          use.append(x)
    for x in aldic:
      belong[x-1]=count
      anslist[x-1]=len(aldic)-len(fr[x-1])-1

for i in range(1,n+1):
  bfs(i)
for i in range(k):
  a,b=map(int,input().split())
  if belong[a-1]==belong[b-1]:
    anslist[a-1]-=1
    anslist[b-1]-=1
for i in range(0,len(anslist)):
  if i!=len(anslist)-1:
    print(anslist[i],end=" ")
  else:
    print(anslist[i])