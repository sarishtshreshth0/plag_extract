n,d=map(int,input().split())
a=[]
for _ in range(n):
  w=list(map(int,input().split()))
  a.append(w)
  
ans=0
for i in range(n-1):
  for j in range(i+1,n):
    c=0
    for f in range(d):
      c+=(a[i][f]-a[j][f])**2
      
    for r in range(0,151):
      if c==r**2:
        ans+=1
        
print(ans)