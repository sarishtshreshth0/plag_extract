from collections import deque,defaultdict

N,M = map(int,input().split())
data = [list(map(int,input().split())) for i in range(M)]

G = defaultdict(list)
for i in range(M):
    G[data[i][0]].append(data[i][1])
    G[data[i][1]].append(data[i][0])

D = [0]+[-1]*(N)

c = 0
for i in range(1,N+1):
    if D[i] != -1:
        continue
    else:
        q = deque([i])
        while q:
            n = q.pop()
            D[n] = 0
            for d in G[n]:
                if D[d] != -1:
                    continue
                else:
                    q.append(d)
        c += 1

print(c)