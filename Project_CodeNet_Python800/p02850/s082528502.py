from collections import deque
N = int(input())
A = [[] for i in range(N)]
B = []
for i in range(N-1):
  a = list(map(int, input().split()))
  A[a[0]-1].append([a[1]-1, 0])
  A[a[1]-1].append([a[0]-1, 1])
  B.append(a)
K = 0
D = {}
C = [0 for i in range(N)]
de = deque([[0, -1]])
while len(de):
  n = de.pop()
  C[n[0]] = 1
  color = 1
  for a in A[n[0]]:
    if C[a[0]] == 1:
      continue
    if color == n[1]:
      color += 1
    if a[1] == 0:
      D[str(n[0])+","+str(a[0])] = color
    else:
      D[str(a[0])+","+str(n[0])] = color
    de.append([a[0], color])
    K = max(K, color)
    color += 1
print(K)
for b in B:
  print(D[str(b[0]-1)+","+str(b[1]-1)])