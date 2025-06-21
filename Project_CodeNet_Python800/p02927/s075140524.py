m, d = map(int, input().split())
ans = 0
if d <= 21:
  ans = 0
else:
  for i in range(m):
    i += 1
    for j in range(21, d):
      j += 1
      d1 = int(str(j)[0])
      d2 = int(str(j)[1])
      if d1 * d2 == i and d1 >= 2 and d2 >= 2:
        ans += 1
print(ans)