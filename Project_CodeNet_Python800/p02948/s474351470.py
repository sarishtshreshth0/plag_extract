from heapq import*
(N,M),*t=[map(int,s.split())for s in open(0)]
q=[0]*50*M
v=[[]for _ in q]
for a,b in t:v[a-1]+=b,
print(sum(([heappush(q,-j)for j in i],-heappop(q))[1]for i in v[:M]))