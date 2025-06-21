import numpy as np

n,d=map(int,input().split())
X=[]
for i in range(n):
  x=np.array(list(map(int,input().split())))
  X.append(x)
count=0
for i in range(n-1):
  for j in range(i+1,n):
    d = ((X[i]-X[j])**2).sum()**.5
    if d==int(d):count+=1
print(count)