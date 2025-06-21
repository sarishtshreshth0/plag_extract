from math import factorial

n,a,b = map(int,input().split())
MOD = 10**9 + 7
xa = 1
xb = 1

k1 = pow(2,n,MOD)
A = pow(factorial(a),MOD-2,MOD)
B = pow(factorial(b),MOD-2,MOD) 

for i in range(a):
  xa = xa*(n-i)%MOD
for j in range(b):
  xb = xb*(n-j)%MOD

ans = (k1 - (A*xa) - (B*xb) - 1)%MOD 

print(ans)