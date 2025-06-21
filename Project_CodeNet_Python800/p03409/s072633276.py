N = int(input())
point = []
for i in range(2*N):
  x, y = map(int, input().split())
  point.append((x, y, i>=N))

point.sort()

ans = 0
Y = set()
for x, y, color in point:
  if color == 0:
    Y.add(y)
  else:
    t = -1
    for _y in Y:
      if t < _y < y:
        t = _y
    if t != -1:
      ans += 1
      Y.discard(t)

print(ans)