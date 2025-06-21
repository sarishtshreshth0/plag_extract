import numpy as np
n, d = map(int, input().split())
x = [np.array(list(map(int, input().split()))) for _ in range(n)]
cnt = 0
for i in range(len(x)-1):
  x_i = x[i]
  for j in x[i+1:]:
    m = x_i - j
    if float(np.linalg.norm(m)).is_integer():
      cnt += 1
print(cnt)
