import math
n,m=map(int,input().split())
data = []
ans = 0
for i in range(n):data.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if(i>=j):continue
    t = 0
    for k in range(m):
      
      t += (data[i][k] - data[j][k])**2
    
    res = math.sqrt(t)
    if(res == int(res)):ans+=1
print(ans)