import heapq  # heapqライブラリのimport
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
lsta=[[] for i in range(10**5+1)]
lst=[]
ans=0
for i in range(N):
 A,B=map(int,input().split())
 lsta[A].append(-B)
heapq.heapify(lst)  # リストを優先度付きキューへ
for i in range(1,M+1):
 for j in lsta[i]:
  heapq.heappush(lst, j)
 if lst!=[]:
  ans+=heapq.heappop(lst)
print(-ans)
