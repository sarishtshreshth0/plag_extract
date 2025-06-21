N ,a, b = map(int,input().split())
MOD = pow(10,9) + 7

A = 1  
for i in range(a):
  A = A*(N-i)*pow(i+1,MOD-2,MOD)%MOD

B = 1  
for i in range(b):
  B = B*(N-i)*pow(i+1,MOD-2,MOD)%MOD

alll = pow(2,N,MOD) -1
#nota = cmb(N,a,MOD)
#notb = cmb(N,b,MOD)
ans = alll - (A+B)
ans = ans%MOD
print(ans)