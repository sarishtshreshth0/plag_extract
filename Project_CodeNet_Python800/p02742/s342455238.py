H, W = map(int, input().split())
 
ans = 0
 
if H%2==0:
  a = H // 2
  b = H // 2
else:
  a = H // 2 + 1
  b = H // 2

if H==1 or W==1:
  ans = 1
elif W%2==0:
  ans = a * (W // 2) + b * (W // 2)
else:
  ans = a * (W // 2 + 1) + b * (W // 2)

print(ans)
