import math
N, D = map(int, input().split( ))
A = []
def d(a,b):
  s = 0
  for i in range(len(a)):
    s += (a[i] - b[i])**2
  return math.sqrt(s)

for _ in range(N):
  A.append(list(map(int, input().split( ))))
ans = 0
for i in range(N):
  for j in range(i+1,N):
    s = d(A[i],A[j])
    if s.is_integer():
      ans += 1
print(ans)  