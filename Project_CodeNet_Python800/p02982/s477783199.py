import math

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]

cnt = 0

for i in range(0, n):
  for j in range(i+1, n):
    
    D = math.sqrt(sum((x[i][k] - x[j][k])**2 for k in range(d)))
    if D.is_integer() == True:
      cnt += 1

print(cnt)