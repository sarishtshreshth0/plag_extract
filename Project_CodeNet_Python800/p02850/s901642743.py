from collections import deque
from sys import stdin
nii=lambda:map(int,stdin.readline().split())

n=int(input())
l=[list(nii()) for i in range(n-1)]

tree=[[] for i in range(n)]
for a,b in l:
  a-=1
  b-=1
  tree[a].append(b)
  tree[b].append(a)

ans_num=0
for i in tree:
  ans_num=max(ans_num,len(i))

col=[-1 for i in range(n)]
col[0]=0

que=deque()
que.append(0)

ans_dict={}
while que:
  x=que.popleft()

  t_col=1
  for i in tree[x]:
    if col[i]!=-1:
      continue
    if t_col==col[x]:
      t_col+=1
    que.append(i)
    col[i]=t_col
    ans_dict[(x+1,i+1)]=t_col
    ans_dict[(i+1,x+1)]=t_col
    t_col+=1

print(ans_num)
for i in l:
  print(ans_dict[tuple(i)])