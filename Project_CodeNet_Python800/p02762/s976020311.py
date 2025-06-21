# 4 4 1
# 2 1
# 1 3
# 3 2
# 3 4
# 4 1

inp = input
MAXX = 10**5 + 5

def bfs(NN, adj, visited, node, comp, ncomp):
    compsize = 0
    while len(node) > 0:
        newnode = []
        for n in node:
            comp[n] = ncomp
            compsize += 1
            for a in adj[n]:
                if visited[a] == False:
                    visited[a] = True
                    newnode.append(a)
        node = newnode

    return compsize


###############################
N, M, K = map(int, inp().split())
adj = [[] for _ in range(N+1)]
nfriend = [0]*(N+1)
nblock = [0]*(N+1)
for m in range(M):
    a, b, = map(int, inp().split())
    adj[a].append(b)
    adj[b].append(a)
    nfriend[a] += 1
    nfriend[b] += 1

comp = [0]*(N+1)
compsize = [0]
ncomp = 0
visited = [False]*(N+1)

for n in range(1, N+1):
    if comp[n] <= 0:
        visited[n] = True
        csize = bfs(N, adj, visited, [n], comp, ncomp+1)
        if csize > 0:
            ncomp += 1
            compsize.append(csize)

for k in range(K):
    c, d = map(int, inp().split())
    if comp[c] == comp[d]:
        nblock[c] += 1
        nblock[d] += 1

ans = ""
for n in range(1, N+1):
    can = compsize[comp[n]] - nfriend[n] - nblock[n] - 1
    ans += str(can)
    if n == N:
        ans += "\n"
    else:
        ans += " "

print(ans)


