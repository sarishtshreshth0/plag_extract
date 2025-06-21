import math
n,d=map(int,input().split())
plot=[list(map(int,input().split())) for i in range(n)]
res=0
for i in range(n-1):
  for j in range(i+1,n):
    dist=0
    for k in range(d):
      dist += (plot[j][k]-plot[i][k])**2
    temp = int(math.sqrt(dist))
    if temp ** 2 == dist:
        res += 1
    
print(res)