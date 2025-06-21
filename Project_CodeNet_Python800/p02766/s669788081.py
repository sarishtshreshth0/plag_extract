n,k = map(int,input().split())
ans = 0
m = 1
while m <= n:
  m *= k
  ans += 1
print(ans)
