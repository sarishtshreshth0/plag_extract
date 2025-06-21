n = int(input())
W = list(map(int,input().split()))
ans = sum(W)
for t in range(1,100):
  x = 0
  y = 0
  for i in range(n):
    if i<=t:
      x+=W[i]
    else:
      y+=W[i]
  ans = min(ans,abs(x-y))
print(ans)
