from collections import defaultdict,deque

graph = defaultdict(list)
N, *AB = map(int, open(0).read().split())
for a, b in zip(*[iter(AB)] * 2):
    graph[a].append(b)


stack = deque([1])
C = [0] * (N + 1)
while stack:
    v = stack.popleft()
    c = 0
    for w in graph[v]:
        c += 1 + (c + 1 == C[v])
        C[w] = c
        stack.append(w)
        
print(max(C))
print("\n".join(str(C[b]) for b in AB[1::2]))