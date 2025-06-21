N,D = map(int,input().split())
X = []
count = 0

for n in range(N):
  x = list(map(int,input().split()))
  X.append(x)
  
for i in range(N):
  for j in range(i+1,N):
    distance = 0
    for k in range(D):
      distance += abs(X[i][k] - X[j][k])**2 
    if (distance**0.5).is_integer():
      count += 1
      
print(count)