import sys
sys.setrecursionlimit(10 ** 9)

N, M, K = map(int, input().split())

Friend = [[] for i in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  Friend[A-1].append(B-1)
  Friend[B-1].append(A-1)

Block = [set() for i in range(N)]
for _ in range(K):
  C, D = map(int, input().split())
  Block[C-1].add(D-1)
  Block[D-1].add(C-1)


def dfs(x):
    if seen[x] == 0:
        R[cnt].add(x)
        seen[x]=1
        for i in Friend[x]:
            dfs(i)

seen = [0]*N
cnt  = 0
R    = []
for i in range(N):
    if seen[i] == 0:
        R.append(set())
        dfs(i)
        cnt += 1

seq = [0]*N

for r in R:
    lr = len(r)
    for j in r:
        seq[j] = lr - len(Friend[j]) - len(r&Block[j]) - 1

print(*seq)