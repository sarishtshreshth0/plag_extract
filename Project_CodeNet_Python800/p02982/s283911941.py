N,D=map(int,input().split())
A=[]
for i in range(N):
  A.append(list(map(int,input().split())))
sum=0
count=0
for i in range(N):
  for j in range(i+1,N):
    for k in range(D):
      sum+=(A[i][k]-A[j][k])**2
    sum=(sum)**0.5
    if sum.is_integer():
      count+=1
    sum=0
print(count)