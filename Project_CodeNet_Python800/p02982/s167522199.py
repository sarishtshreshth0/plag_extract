n,d=[int(x) for x in input().split()]
x=[]
for i in range(n):
  X=[int(x) for x in input().split()]
  x.append(X)
ans=0
for i in range(n-1):
  for j in range(i+1,n):
    dis=0
    for k in range(d):
      dis+=(x[i][k]-x[j][k])**2
    for l in range(181):
      if dis==l**2:
        ans+=1
        break
print(ans)