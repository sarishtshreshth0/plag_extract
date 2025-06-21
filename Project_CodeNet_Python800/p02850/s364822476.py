from collections import deque
from sys import stdin
nii=lambda:map(int,stdin.readline().split())

n=int(input())
l=[list(nii()) for i in range(n-1)]

tree=[[]for _ in range(n)]
for a,b in l:
  a-=1
  b-=1
  tree[a].append(b)
  tree[b].append(b)

ans_num=0
for i in tree:
  ans_num=max(ans_num,len(i))

dq=deque()
dq.append((0,0))

seen=set()
seen.add(0)

ans_dict={}
while dq:
  x,color=dq.pop()

  i=0
  for nx in tree[x]:
    if nx in seen:
      continue

    i+=1
    if i==color:
      i+=1

    seen.add(nx)
    dq.append((nx,i)),
    ans_dict[x+1,nx+1]=i
    ans_dict[nx+1,x+1]=i

print(ans_num)
for i in l:
  print(ans_dict[tuple(i)])