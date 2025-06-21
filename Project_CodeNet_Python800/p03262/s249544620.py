import numpy as np

N, X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x.sort()

y = []

for i in range(N):
  y.append(x[i + 1] - x[i])
  
ans = y[0]

#print(x)
#print(y)
  
for i in range(N - 1):
  #print(ans, y[i+1])
  g = np.gcd.reduce([ans, y[i + 1]])
  #print(g)
  if g == 1:
    print(1)
    break
  else:
    ans = g
else:
  print(ans)