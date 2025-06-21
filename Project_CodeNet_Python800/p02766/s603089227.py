n, k = map(int, input().split())
t = k
ans = 1
while t <= n:
  t = t * k
  ans += 1
print(ans)