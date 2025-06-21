import heapq

#N is numbers of BAITO, M is limit of days
N,M=map(int,input().split())
 
i=0
inp ={}
while i<N:
  readTime,inCome=map(int,input().split())
  if readTime in inp:
    inp[readTime].append(-inCome)
  else:
    inp[readTime]=[-inCome]
  
  i=i+1
 
#print(inp)  
 
result=0
pool=[]
heapq.heapify(pool)
i=1
while i<=M:
  if i in inp:
    for k in inp[i]:
      heapq.heappush(pool,k)
  if len(pool)>0:
    result=result-heapq.heappop(pool)
  i=i+1
 
print(result)
