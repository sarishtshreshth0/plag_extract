n = int(input())
AB = [[] * 2 for _ in range(n - 1)]
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
	a, b = map(int, input().split())
	AB[i].append(a)
	AB[i].append(b)
	graph[a].append(b)
	graph[b].append(a)

root = 1
parent = [0] * (n + 1)
order = []
stack = [root] # 根を stack に入れる

while stack:
	x = stack.pop()
	order.append(x)
	for y in graph[x]:
		if y == parent[x]:
			continue
		parent[y] = x
		stack.append(y)

color = [-1] * (n + 1)
for x in order:
	ng = color[x]
	c = 1
	for y in graph[x]:
		if y == parent[x]:
			continue
		if c == ng:
			c += 1
		color[y] = c
		c += 1

res = []
for a, b in AB:
	if parent[a] == b:
		res.append(color[a])
	else:
		res.append(color[b])

print(max(res)) # root
print('\n'.join(map(str, res)))