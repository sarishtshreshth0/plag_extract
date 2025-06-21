n, d = map(int, input().split())
lst = []
for _ in range(n):
  x = list(map(int, input().split()))
  lst.append(x)
ans = 0
for i in range(n-1):
  for j in range(i+1, n):
    dist = 0
    for k in range(d):
      dist += (lst[i][k] - lst[j][k])**2
    j = 1
    while j**2 <= dist:
      if j**2 == dist:
        ans += 1
        break
      j += 1
print(ans)