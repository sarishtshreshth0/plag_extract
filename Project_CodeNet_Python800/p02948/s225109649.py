import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

ablist=[]
for i in range(N):
  A,B=map(int,input().split())
  ablist.append((A,B))
ablist.sort(reverse=True)
  
hq=[]
answer=0
for i in reversed(range(M)):
  while ablist:
    a,b=ablist[-1]
    if i+a<=M:
      ablist.pop()
      heapq.heappush(hq,((-b,a)))
    else:
      break
  
  if hq:
    mb,a=heapq.heappop(hq)
    answer-=mb
    #print(i,a+i,-mb)
    
print(answer)