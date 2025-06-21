n,m=map(int,input().split())
x=list(map(int,input().split()))
ans=0
x.sort()
y=[0]*(m-1)
for i in range(m-1):
  y[i]=x[i+1]-x[i]
y.sort()
y=y[:max(0,m-n)]
print(sum(y))