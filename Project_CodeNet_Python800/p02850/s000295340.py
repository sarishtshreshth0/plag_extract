import collections
n = int(raw_input())
adj = collections.defaultdict(list)
edges = []
for _ in range(n - 1):
	u,v = map(int, raw_input().split(' '))
	edges.append((u,v))
	adj[u].append(v)
	adj[v].append(u)
root = 1
q = collections.deque([root])
h = {}
while(q):
	u = q.popleft()
	c = 1

	used = set([h[tuple(sorted([u,v]))] for v in adj[u] if tuple(sorted([u,v])) in h]) 

	for v in adj[u]:
		t = tuple(sorted([u,v])) 
		if t not in h:
			while(c in used): c+=1
			h[t] = c	
			c+=1
			q.append(v)
print max(h.values())
for u,v in edges:
	print h[(u,v)]