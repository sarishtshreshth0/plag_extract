from itertools import combinations
import math


n, d = map(int, input().split())

xn = []
for i in range(n):
  x = [int(num) for num in input().split()]
  xn.append(x)
  
answer =  0
for i,j in combinations(range(n),2):
    sum = 0.0
    for k in range(d):
        sum += (xn[i][k]-xn[j][k])**2
    if math.sqrt(sum).is_integer():
        answer += 1
 
print(answer)