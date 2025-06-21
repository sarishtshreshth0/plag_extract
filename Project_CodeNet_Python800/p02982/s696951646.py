N,D=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
l=len(X)
c=0
for i in range(l):
 for j in range(i+1,l):
  t=sum((X[i][d]-X[j][d])**2for d in range(D))**0.5
  c+=t==int(t)
print(c)