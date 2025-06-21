import math

n=int(input())
a=list(map(int,input().split()))

b=list(reversed(a))

g=[]
g.append(a[0])
for i in range(1,n):
  x=math.gcd(g[-1],a[i])
  g.append(x)

h=[]
h.append(b[0])
for j in range(1,n):
  y=math.gcd(h[-1],b[j])
  h.append(y)
  
ans=[]
for k in range(n):
  if k==0:
    ans.append(h[n-2])
  elif k==n-1:
    ans.append(g[n-2])
  else:
    e=g[k-1]
    f=h[n-1-k-1]
    ans.append(math.gcd(e,f))
    
print(max(ans))