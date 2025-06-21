import math
N,D = map(int,input().split())
Xs = [list(map(int,input().split()))for i in range(N)]
c = 0
for i in range(N-1):
  X1 = Xs[i]
  for j in range(i+1,N):
    X2 = Xs[j]
    su = 0
    for k in range(D):
      su += abs(X1[k]-X2[k]) **2
    distance = math.sqrt(su)
    if distance.is_integer():
      c+=1
print(c)