from collections import deque
N, M, K = map(int, input().split())
A = [[] for i in range(N)]
B = [[] for i in range(N)]
for i in range(M):
  a, b = map(lambda x:int(x)-1, input().split())
  A[a].append(b)
  A[b].append(a)
for i in range(K):
  a, b = map(lambda x:int(x)-1, input().split())
  B[a].append(b)
  B[b].append(a)
P = [-1 for i in range(N)]
Q = []
k = -1
for i in range(N):
  if P[i] == -1:
    q = 1
    k += 1
    P[i] = k
    d = deque([i])
    while len(d):
      s = d.pop()
      for t in A[s]:
        if P[t] == -1:
          P[t] = k
          q += 1
          d.append(t)
    Q.append(q)
for i in range(N):
  ans = Q[P[i]] - len(A[i]) - 1
  for j in B[i]:
    if P[i] == P[j]:
      ans -= 1
  print(ans)