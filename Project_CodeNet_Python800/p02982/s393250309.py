N,D=map(int,input().split())
res = 0
List = []
for i in range (N):
  List.append(list(map(int, input().split())))
  
def calcDist(ListX,a,b):
  n = 0
  for k in range(D):
    x = ListX[a][k] - ListX[b][k]
    n += x*x
  n = n ** 0.5
  nn = int(n)
  if n-nn > 0:
    return False
  else:
    return True

for i in range(N):
  for j in range(N):
    if i == j:
      pass
    else:
      if calcDist(List,i,j):
        res += 1
res = res //2
print(res)