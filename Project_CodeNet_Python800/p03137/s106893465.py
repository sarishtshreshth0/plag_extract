import sys
n,m=map(int,input().split())
x=sorted(list(map(int,input().split())))
dp=[0]*(m-1)
ans=0

if n>=m:
  print(0)
  sys.exit()
for i in range(m-1):
  dp[i]=x[i+1]-x[i]
dp.sort()

for i in range(m-n):
  ans+=dp[i]
print(ans)