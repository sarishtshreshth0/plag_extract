import math
N,X=map(int,input().split())
L=list(map(int,input().split()))
L.append(X)
L=sorted(L)
m=L[1]-L[0]
for i in range(N):
  m=math.gcd(m,L[i+1]-L[i])
print(m)