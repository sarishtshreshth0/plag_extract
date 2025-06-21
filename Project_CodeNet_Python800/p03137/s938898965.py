n,m=map(int,input().split())
a=list(map(int,input().split()))

a=sorted(a)
b=[]

for x in range(m-1):
  c=a[x+1]-a[x]
  b.append(c)
  

b=sorted(b)
if n>=m:
  print(0)
  
else:
  nn=m-n
  ans=0
  for u in range(nn):
    ans+=b[u]
    
  print(ans)