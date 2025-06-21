import sys
N,M = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
if N >= M:
    print(0)
    sys.exit()
X = sorted(X)
dis = [0 for x in range(M-1)]
for i in range(M-1):
    dis[i] = X[i+1] - X[i]
dis.sort()
dis.reverse()
for i in range(N-1):
    dis[i] = 0
print(sum(dis))
