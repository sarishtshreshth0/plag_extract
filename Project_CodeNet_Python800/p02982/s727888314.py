import math
from itertools import combinations
N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]

combination = list(combinations(range(N),2))

cnt = 0
for i,j in combination:
  distance = 0
  for k in range(D):
    distance += abs(X[i][k] - X[j][k]) ** 2
  distance = math.sqrt(distance)
  if distance == math.floor(distance):
    cnt += 1
    
print(cnt)