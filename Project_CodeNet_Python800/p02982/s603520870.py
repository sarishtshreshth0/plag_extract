N,D = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(N)]

def isSquare(x):
  f = 1
  while f * f <= x:
    if f * f == x:
      return True
    else:
      f += 1
  return False
  
def calcSquareOfDistance(p1,p2,dimension):
  s = 0
  for i in range(dimension):
    s += (p1[i] - p2[i])**2
  return s

def judge(p1,p2,dimension):
  return isSquare(calcSquareOfDistance(p1,p2,dimension))

ans = 0
for i in range(N-1):
  for j in range(i+1,N):
    if judge(a[i],a[j],D):
      ans += 1
print(ans)