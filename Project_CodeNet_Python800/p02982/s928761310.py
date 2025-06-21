#! python3
#  solve_133B.py

import math



N,D = map(int,input().split())
X = []
ans = 0


def dis(Y,Z):
    ans = 0
    for i in range(D):
        ans += (Y[i] - Z[i])**2
    return math.sqrt(ans)

for i in range(N):
    X.append(list(map(int,input().split())))

for i in range(N):
    for j in range(i+1,N):
       if dis(X[i],X[j]) % 1 == 0:
           ans += 1

print(ans)