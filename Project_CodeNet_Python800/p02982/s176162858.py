import itertools
import numpy as np

n, d = map(int, input().split())
Dist = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for d_list in list(itertools.combinations(Dist, 2)):
  x = np.array(d_list[0])
  y = np.array(d_list[1])
  tmp = 0
  for i in (x-y):
    tmp += i*i
  k = tmp**0.5
  if k == int(k):
    ans += 1

print(ans)