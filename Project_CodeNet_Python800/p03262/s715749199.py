import numpy as np
import math

N,X=map(int,input().split())
L=np.array(list(map(int,input().split())))
L=abs(L-X)
ans=L[0]

for i in range(1,N):
  ans=math.gcd(ans,L[i])
print(ans)