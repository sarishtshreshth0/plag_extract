n = int(input())
p = [list(map(int,input().split()))+[0] for _ in range(n)]
p += [list(map(int,input().split()))+[1] for _ in range(n)]
p.sort()
ans = 0
l = set()
for x, y, c in p:
  if c == 0:
    l.add(y)
  else:
    t = -1
    for y_dash in l:
      if t < y_dash < y:
        t = y_dash
    if t != -1:
      ans += 1
      l.discard(t)
print(ans)