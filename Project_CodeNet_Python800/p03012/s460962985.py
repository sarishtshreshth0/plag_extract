import math
inp = int(input())
var = list(map(int,input().split()))
l = []
for i in range(inp-1):
  a = math.fabs(sum(var[0:i+1]) - sum(var[i+1:inp+1]))
  l.append(a)
print(int(min(l)))