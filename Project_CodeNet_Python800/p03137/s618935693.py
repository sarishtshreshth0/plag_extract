n,m=map(int,input().split())
if n>=m:
  print(0)
  import sys
  sys.exit()
x=list(map(int,input().split()))
x.sort()
l=[]
for i in range(m-1):
  l.append(x[i+1]-x[i])
l.sort()
sm=0
for j in range(m-n):
  sm+=l[j]
print(sm)