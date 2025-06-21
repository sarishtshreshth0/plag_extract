import math
n,k = map(int, input().split())

N = int(math.floor(math.log(n)/math.log(k)))+1
m = n
L = []
for i in range(N+1):
  L.append(m//(k**(N-i)))
  m = m%(k**(N-i))
  
if L[0] == 0:
  L.pop(0)

print(len(L))