import sys
sys.setrecursionlimit(3*10**5)

N, M = map(int,input().split())
adj = [[] for i in range(N+1)]
for i in range(M):
	u, v, w = map(int,input().split())
	adj[u].append(v)
	adj[v].append(u)

vis = [False for i in range(N+1)]
def bfs(s):
	frontier = [s]
	ptr = 0
	while ptr < len(frontier):
		u = frontier[ptr]
		if not vis[u]:
			vis[u] = True
			for v in adj[u]:
				if not vis[v]:
					frontier.append(v)
		ptr += 1
ans = 0
for u in range(1,N+1):
	if not vis[u]:
		ans += 1
		bfs(u)

print(ans)
