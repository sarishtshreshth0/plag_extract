import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
if N>M:
  N = M
Xs = list(mapint())
Xs.sort()
dist = []
for i in range(1, M):
    dist.append(Xs[i]-Xs[i-1])
dist.sort()

print(sum(dist[:M-N]))