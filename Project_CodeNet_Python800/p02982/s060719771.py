import math

n,d=map(int, input().split())
l=[]*n
for i in range(n):
  x=list(map(int, input().split()))
  l.append(x)

cnt=0
for i in range(n):
  for j in range(i+1,n):
    dis=0
    for k in range(d):
      dis += (l[i][k]-l[j][k])**2
    dis = math.sqrt(dis)

    if dis==math.floor(dis):
      cnt+=1
print(cnt)