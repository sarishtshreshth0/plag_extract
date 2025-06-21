from collections import deque
N = int(input())
node_branch = [[] for _ in range(N+1)]
branch = [0] * (N)
link = [0] * (N+1)
checked = [False] * (N+1)

for num in range(N - 1):
    a, b = map(int, input().split())
    node_branch[a].append((b, num+1))
    node_branch[b].append((a, num+1))

maxlen = 0
for i, node in enumerate(node_branch):
    if maxlen < len(node):
        maxlen = len(node)
        maxnode = i

print(maxlen)

d = deque()
d.append(maxnode)
link[1] = 0
checked[maxnode] = True

while len(d)>0:
    now = d.popleft()
    color = 1
    for n, b in node_branch[now]:
        if checked[n]:
            continue
        if color == link[now]:
            color += 1
        branch[b] = color
        link[n] = color
        color += 1
        checked[n] = True
        d.append(n)

for i in range(1, N):
    print(branch[i])