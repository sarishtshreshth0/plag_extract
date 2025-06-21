n = int(input())
r = sorted([list(map(int, input().split())) for i in range(n)])
b = sorted([list(map(int, input().split())) for i in range(n)])
ans = 0
for bx,by in b:
  now_ry = -1
  now_index = -1
  for key,(rx,ry) in enumerate(r):
    if bx > rx and by > ry and ry > now_ry:
      now_ry = ry
      now_index = key
  if now_ry >= 0:
    ans += 1
    r.pop(now_index)
print(ans)
