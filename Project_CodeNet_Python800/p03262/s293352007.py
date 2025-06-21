from math import gcd 
N, X = list(map(int, input().split()))
x = list(map(int, input().split()))
if(N == 1): print(abs(x[0] - X))
else:
  ans = gcd(abs(x[0] - X), abs(x[1] - X))
  for i in range(2, N):
  	ans = gcd(ans, abs(x[i] - X))
    
  print(ans)