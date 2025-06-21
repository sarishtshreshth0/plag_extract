import queue
n=int(input())
cf=[0]*n
cg=[0]*(n-1)
ce=[[] for _ in range(n)]
e=[[]for _ in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  e[a-1]+=[b-1]
  e[b-1]+=[a-1]
  ce[a-1]+=[i]
  ce[b-1]+=[i]
k=len(max(e,key=len))
q=queue.Queue()
q.put(0)
while not q.empty():
  now=q.get()
  cf[now]=1
  c=0
  for i in ce[now]:
    if cg[i]:c=cg[i]
  j=1
  for i in ce[now]:
    if j==c:j+=1
    if cg[i]:continue
    cg[i]=j
    j+=1
  for i in e[now]:  
    if cf[i]:continue
    q.put(i)
print(k)
for i in cg:
  print(i)