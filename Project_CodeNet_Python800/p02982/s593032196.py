N,D=map(int,input().split())
ans=0
A=[]
for x in range(N):
  X=list(map(int,input().split()))
  for y in range(len(A)):
    s=0
    for z in range(D):
      s+=(A[y][z]-X[z])**2
    if ((s**(1/2))*10)%10==0:
      ans+=1
  A.append(X)
print(ans)