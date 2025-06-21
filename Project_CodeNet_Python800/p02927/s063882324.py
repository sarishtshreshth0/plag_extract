M, D = map(int, input().split())

ans = 0
for m in range(1, M+1):
  for d1 in range(2, 10):
    if m % d1 == 0:
      d10 = m // d1
      if 2 <= d10 <= 9 and 10*d10 + d1 <= D:
        ans += 1

print(ans)