import math
import numpy as np
N,D = map(int,input().split())
X = np.array([list(map(int,input().split())) for n in range(N)])
ans = 0

for n in range(N):
  for m in range(N):
    d = 0
    for x,y in zip(X[n],X[m]):
      d += (x-y)**2
    if math.sqrt(d).is_integer() and d != 0:
      ans+=1
        
print(ans//2)