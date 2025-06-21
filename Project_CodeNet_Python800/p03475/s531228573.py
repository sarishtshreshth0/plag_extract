from collections import deque

N = int(input())

CSFs = [list(map(int, input().split())) for _ in range(N-1)]

h = deque([0])

for i in range(N-2,-1,-1):
  t = CSFs[i][1]
  t += CSFs[i][0]
  for j in range(i+1,N-1):
    if t < CSFs[j][1]:
      t = CSFs[j][1]
    else:
      if t%CSFs[j][2] > 0:
        t += CSFs[j][2] - (t%CSFs[j][2])
    t += CSFs[j][0]
  h.appendleft(t)
  
while h:
  print(h.popleft())