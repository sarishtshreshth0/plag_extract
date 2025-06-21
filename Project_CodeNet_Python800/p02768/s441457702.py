n, a, b = map(int, input().split())
ans = pow(2,n,10**9+7)-1

A = 1
for i in range(1,a+1):
  A = (A*(n-i+1))%(10**9+7)
  x = pow(i,10**9+5,10**9+7)
  A *= x

B = 1
for i in range(1,b+1):
  B = (B*(n-i+1))%(10**9+7)
  y = pow(i,10**9+5,10**9+7)
  B *= y

ans = ans-A-B
if ans < 0:
  ans = ans+10**9+7
ans = int(ans%(10**9+7))
print(ans)