from collections import deque
n, m = map(int, input().split())
tree = [[] for i in range(n)]

for i in range(m):
  x, y, z = map(int, input().split())
  tree[x-1].append(y-1)
  tree[y-1].append(x-1)

already = [False]*n
ans = 0
for i in range(n):
  if already[i]:
    continue
  ans += 1
  not_yet = deque(tree[i])
  for value in tree[i]:
    already[value] = True
  while not_yet:
    key = not_yet.popleft()
    for value in tree[key]:
      if already[value]:
        continue
      already[value] = True
      not_yet.append(value)
print(ans)